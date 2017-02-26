#!/usr/bin/env python3

import apt_pkg
from sys import argv,exit,stderr

if len(argv) < 2:
	print("Usage: {} <package> [more packages]".format(argv[0]))
	print("\tPrint Build-Depends for each given source package.")
	sys.exit(0)

params = argv[1:]

apt_pkg.init_config()
apt_pkg.init_system()

for pkg in params:
	stderr.write("[#] Looking {} up...\n".format(pkg))
	srcrec = apt_pkg.SourceRecords()
	if not srcrec.lookup(pkg):
		stderr.write("[-] Could not find package {}\n".format(pkg))
		continue
	pkg_build_deps = srcrec.build_depends['Build-Depends']
	for pkg_dep_name in map(lambda el: el[0][0], pkg_build_deps):
 	   print(pkg_dep_name)
