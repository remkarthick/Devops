# Install Open Ldap in Ubuntu

sudo apt install slapd ldap-utils

# Check Status

sudo systemctl status slapd


# Configure LDAP

sudo dpkg-reconfigure slapd

## Verify if slapd is configured properly

kk@kkbox:~$ sudo tree /etc/ldap/slapd.d
/etc/ldap/slapd.d
├── cn=config
│   ├── cn=module{0}.ldif
│   ├── cn=schema
│   │   ├── cn={0}core.ldif
│   │   ├── cn={1}cosine.ldif
│   │   ├── cn={2}nis.ldif
│   │   └── cn={3}inetorgperson.ldif
│   ├── cn=schema.ldif
│   ├── olcDatabase={0}config.ldif
│   ├── olcDatabase={-1}frontend.ldif
│   └── olcDatabase={1}mdb.ldif
└── cn=config.ldif

2 directories, 10 files

# Create a new file "add_entries.ldif" with below content inside

dn: ou=Employee,dc=practice,dc=com
objectClass: organizationalUnit
ou: Employee

dn: ou=Groups,dc=practice,dc=com
objectClass: organizationalUnit
ou: Groups

dn: cn=developers,ou=Groups,dc=practice,dc=com
objectClass: posixGroup
cn: developers
gidNumber: 5000

dn: uid=allen,ou=Employee,dc=practice,dc=com
objectClass: inetOrgPerson
objectClass: posixGroup
objectClass: shadowAccount
uid: allenjoe
sn: joe
givenName: allen
cn: Allen Joe
displayName: Allen Joe
uidNumber: 10000
gidNumber: 5000
userPassword: allen123
loginShell: /bin/bash
homeDirectory: /home/allen

dn: uid=bob,ou=Employee,dc=practice,dc=com
objectClass: inetOrgPerson
objectClass: posixGroup
objectClass: shadowAccount
uid: bobstanly
sn: stanly
givenName: bob
cn: Bob Stanly
displayName: Bob Stanly
uidNumber: 10001
gidNumber: 5000
userPassword: bob123
loginShell: /bin/bash
homeDirectory: /home/bob
