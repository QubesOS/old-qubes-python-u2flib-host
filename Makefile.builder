DEBIAN_BUILD_DIRS.vm-stretch := debian
DEBIAN_BUILD_DIRS := $(DEBIAN_BUILD_DIRS.$(PACKAGE_SET)-$(DIST))
RPM_SPEC_FILES.vm := rpm_spec/python3-u2flib-host.spec
RPM_SPEC_FILES := $(RPM_SPEC_FILES.$(PACKAGE_SET))
# vim: ft=make
