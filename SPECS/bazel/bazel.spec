%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%global debug_package %{nil}
%define __os_install_post %{nil}

Summary: Build software of any size, quickly and reliably, just as engineers do at Google.
Name:		bazel
Version:	0.24.1
Release:	1%{?dist}
License:	Apache License 2.0
Group: 		Development/Tools
URL: 		http://bazel.build/
Source:  	https://github.com/bazelbuild/bazel/releases/download/0.24.1/bazel-0.24.1.tar.gz
%define sha1    bazel=0534138766c04244aeec5b607b4561b42f61cbdf
Requires: 	openjdk
BuildRequires:  openjdk zlib-devel which findutils tar gzip zip unzip
BuildRequires:  gcc
BuildRequires:  python2

%description
Bazel is Google's own build tool, now publicly available in Beta. Bazel has
built-in support for building both client and server software, including client
applications for both Android and iOS platforms. It also provides an extensible
framework that you can use to develop your own build rules.

%prep
%setup -q

%build
export JAVA_HOME=`echo /usr/lib/jvm/OpenJDK*`
export PYTHONPATH=%{buildroot}%{python2_sitelib}
mkdir /usr/tmp
export TMPDIR=/usr/tmp
./compile.sh
pushd output
./bazel
popd

%install
mkdir -p %{buildroot}/usr/bin
cp output/bazel %{buildroot}/usr/bin/


%files
%defattr(-,root,root)
%attr(777,root,root) /usr/bin/bazel

%changelog
*	Mon Jun 03 2019 Harinadh Dommaraju <hdommaraju@vmware.com> 0.24.1-1
-	Initial packaging for bazel in Photon-1.0
