#!/usr/bin/env python3
"""Validate staged public assets without credentials or third-party Python packages."""
import base64, hashlib, pathlib, re, subprocess, sys, tempfile, xml.etree.ElementTree as ET

incoming, trusted = map(pathlib.Path, sys.argv[1:])
version = (incoming/'version.txt').read_text().strip()
assert re.fullmatch(r'\d+\.\d+\.\d+', version), 'Invalid version'
archive = incoming/f'Custa-{version}-macos-universal.zip'
assert {p.name for p in incoming.iterdir()} == {archive.name, archive.name+'.sha256', 'version.txt', 'appcast.xml', 'release-notes.md'}, 'Unexpected public files'
checksum = (incoming/(archive.name+'.sha256')).read_text().split()
assert len(checksum) == 2 and checksum[1] == archive.name, 'Checksum filename mismatch'
assert hashlib.sha256(archive.read_bytes()).hexdigest() == checksum[0], 'Checksum mismatch'
ns = {'sparkle':'http://www.andymatuschak.org/xml-namespaces/sparkle'}
feed = ET.parse(incoming/'appcast.xml')
items = feed.findall('./channel/item')
assert len(items) == 1, 'Expected one latest update'
item = items[0]
assert item.findtext('sparkle:version', namespaces=ns) == version, 'Feed version mismatch'
assert item.findtext('sparkle:minimumSystemVersion', namespaces=ns) == '14.0.0', 'Minimum system version mismatch'
enclosure = item.find('enclosure')
assert enclosure is not None
assert enclosure.get('url') == f'https://github.com/aliyasirusta/custa-releases/releases/download/v{version}/{archive.name}', 'Unexpected download URL'
assert enclosure.get('length') == str(archive.stat().st_size), 'Archive length mismatch'
signature = base64.b64decode(enclosure.attrib['{'+ns['sparkle']+'}edSignature'], validate=True)
key = base64.b64decode((trusted/'sparkle-public-key.txt').read_text().strip(), validate=True)
assert len(signature) == 64 and len(key) == 32
with tempfile.TemporaryDirectory() as tmp:
    pub, sig = pathlib.Path(tmp)/'public.der', pathlib.Path(tmp)/'signature'
    pub.write_bytes(bytes.fromhex('302a300506032b6570032100') + key)
    sig.write_bytes(signature)
    subprocess.run(['openssl','pkeyutl','-verify','-rawin','-pubin','-keyform','DER','-inkey',str(pub),'-sigfile',str(sig),'-in',str(archive)], check=True)
current = trusted/'appcast.xml'
if current.exists():
    old = ET.parse(current).findtext('./channel/item/sparkle:version', namespaces=ns)
    if old: assert tuple(map(int, version.split('.'))) >= tuple(map(int, old.split('.'))), 'Refusing to downgrade update feed'
print(f'Archive signature, checksum, URL and feed version verified: {version}')
