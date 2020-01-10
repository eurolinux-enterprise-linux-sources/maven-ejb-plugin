Name:           maven-ejb-plugin
Version:        2.3
Release:        8%{?dist}
Summary:        Maven EJB Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-ejb-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins)
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)


Obsoletes: maven2-plugin-ejb <= 0:2.0.8
Provides: maven2-plugin-ejb = 0:%{version}-%{release}

%description
Generates a J2EE Enterprise JavaBean (EJB) file 
as well as the associated client JAR.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

# Install JAR file to %{_javadir}/%{name}.jar
%mvn_file : %{name}

%build
# Skip tests (API incompatibilities with our maven-artifact 2.2.1)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Jul 12 2013 Michal Srb <msrb@redhat.com> - 2.3-8
- Install LICENSE and NOTICE files (Resolves: rhbz#983882)
- Adapt to current guidelines
- Fix BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.3-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3-3
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-1
- Update to 2.3.

* Tue Jul 13 2010 Hui Wang <huwang@redhat.com> - 2.2.1-5
- Skip tests

* Tue Jul 13 2010 Hui Wang <huwang@redhat.com> - 2.2.1-4
- Add missing requires maven2

* Wed Jun 02 2010 Hui Wang <huwang@redhat.com> - 2.2.1-3
- Changed epoch 1 to epoch 0 in provides

* Wed Jun 02 2010 Hui Wang <huwang@redhat.com> - 2.2.1-2
- Added epoch 1 to provides
- Fixed description line length
- Fixed tarball generation svn instruction

* Tue Jun 01 2010 Hui Wang <huwang@redhat.com> - 2.2.1-1
- Initial version of the package
