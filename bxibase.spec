###############################################################################
# $Revision: 1.86 $
# $Date: 2011/07/06 16:54:26 $
###############################################################################

#TODO: define your package name
%define name bxibase

# Bull software starts with 1.1-Bull.1.0
# For versionning policy, please see wiki:
# http://intran0x.frec.bull.fr/projet/HPC/wiki_etudes/index.php/How_to_generate_RPM#Bull_rpm_NAMING_CONVENTION
%define version 2.0.0

# Using the .snapshot suffix helps the SVN tagging process.
# Please run <your_svn_checkout>/devtools/packaged/bin/auto_tag -m
# to get the auto_tag man file
# and to understand the SVN tagging process.
# If you don't care, then, just starts with Bull.1.0%{?dist}.snapshot
# and run 'make tag' when you want to tag.
%define release Bull.1.0%{?dist}.snapshot

# Warning: Bull's continuous compilation tools refuse the use of
# %release in the src_dir variable!
%define src_dir %{name}-%{version}
%define src_tarall %{src_dir}.tar.gz

# Predefined variables:
# {%_mandir} => normally /usr/share/man (depends on the PDP)
# %{perl_vendorlib} => /usr/lib/perl5/vendor_perl/

# Other custom variables
%define src_conf_dir conf
%define src_bin_dir bin
%define src_lib_dir lib
%define src_doc_dir doc

%define target_conf_dir /etc/
%define target_bin_dir /usr/bin
%define target_lib_dir /usr/lib*
%define target_python_lib_dir %{python2_sitelib}
%define target_man_dir %{_mandir}
%define target_doc_dir /usr/share/doc/%{name}

# TODO: Give your summary
Summary:        Implementation of basical functionnality in c like a logger a module of parallelization
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{src_tarall}
# Perform a 'cat /usr/share/doc/rpm-*/GROUPS' to get a list of available
# groups. Note that you should be in the corresponding PDP to get the
# most accurate information!
# TODO: Specify the category your software belongs to
Group:		Development/Libraries
BuildRoot:	%{_tmppath}/%{name}-root
# Automatically filled in by PDP: it should not appear therefore!
#Packager:	Bull <help@bull.net>
Distribution:	Bull HPC

# Automatically filled in by PDP: it should not appear therefore!
#Vendor:         Bull
License:        GPL
BuildArch:	x86_64
URL:	 	https://novahpc.frec.bull.fr

#TODO: What do you provide
Provides: %{name}
#Conflicts:
#TODO: What do you require
Requires: zeromq3
Requires: czmq
Requires: backtrace
Requires: python-cffi >= 0.7.2

#TODO: Give a description (seen by rpm -qi) (No more than 80 characters)
%description
Basic C modules including the high performance BXI logging library. 

###############################################################################
# Prepare the files to be compiled
%prep
#%setup -q -n %{name}
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
%setup
%configure 

###############################################################################
# The current directory is the one main directory of the tar
# Order of upgrade is:
#%pretrans new
#%pre new
#install new
#%post new
#%preun old
#delete old
#%postun old
#%posttrans new
%build
%{__make}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT  %{?mflags_install}
mkdir -p $RPM_BUILD_ROOT/%{target_doc_dir}
cp ChangeLog $RPM_BUILD_ROOT/%{target_doc_dir}


%post

%postun

%preun

%clean
cd /tmp
rm -rf $RPM_BUILD_ROOT/%{name}-%{version}
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

###############################################################################
# Specify files to be placed into the package
%files
%defattr(-,root,root)
#%{_libdir}/lib*
%{_includedir}/bxi/base/*.h
%{target_lib_dir}/lib*
%{target_python_lib_dir}/*



#%config(noreplace) %{target_conf_dir}/my.conf

# Changelog is automatically generated (see Makefile)
# The %doc macro already contain a default path (usually /usr/doc/)
# See:
# http://www.rpm.org/max-rpm/s1-rpm-inside-files-list-directives.html#S3-RPM-INSIDE-FLIST-DOC-DIRECTIVE for details
# %doc ChangeLog
# or using an explicit path:


#%{target_bin_dir}/bin1
#%{target_bin_dir}/prog2
#%{target_bin_dir}/exe3
%doc
     %{target_doc_dir}/ChangeLog
#     %{target_doc_dir}/COPYING

# %changelog is automatically generated by 'make log' (see the Makefile)
##################### WARNING ####################
## Do not add anything after the following line!
##################################################
%changelog

