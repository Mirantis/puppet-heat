Name:          openstack-heat-virtualenv-python-cinderclient
Version:       1.0.5
Release:       1%{?dist}
Summary:       python-cinderclient ionstalled into virtual env for openstack-heat
License:       ASL 2.0
URL:           https://launchpad.net/heat
Source0:       python-cinderclient-%{version}.tar.gz
Source1:       openstack-heat-virtualenv-0.1-1.el6.x86_64.rpm
Source2:       openstack-heat-virtualenv-python-argparse-1.2.1-1.el6.noarch.rpm
Source3:       openstack-heat-virtualenv-python-pbr-0.5.21-1.el6.noarch.rpm
Source4:       openstack-heat-virtualenv-python-requests-1.2.2-1.el6.noarch.rpm
Source5:       openstack-heat-virtualenv-python-simplejson-3.3.0-1.el6.noarch.rpm
Source6:       openstack-heat-virtualenv-python-six-1.3.0-1.el6.noarch.rpm
Source7:       openstack-heat-virtualenv-python-prettytable-0.7.2-1.el6.noarch.rpm
BuildArch:     noarch
 
BuildRequires: python-virtualenv
Requires: python-virtualenv
Requires: openstack-heat-virtualenv
Requires: openstack-heat-virtualenv-python-argparse
Requires: openstack-heat-virtualenv-python-pbr
Requires: openstack-heat-virtualenv-python-requests
Requires: openstack-heat-virtualenv-python-simplejson
Requires: openstack-heat-virtualenv-python-six
Requires: openstack-heat-virtualenv-python-prettytable

#PrettyTable


AutoReqProv: no

Prefix:         /opt/openstack-heat
%global debug_package %{nil}
#%define _binaries_in_noarch_packages_terminate_build   0


%description
webo in virtual environment for openstack-heat


%build

rm -rf  %{_builddir}%{prefix}

export PYTHONPATH=$PWD:${PYTHONPATH}
venv=%{_builddir}%{prefix}

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE1
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE2
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE3
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE4
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE5
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE6
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE7

source $venv/bin/activate

$venv/bin/pip install %SOURCE0


# Cleanup    
rpm -e openstack-heat-virtualenv-python-prettytable
rpm -e openstack-heat-virtualenv-python-requests
rpm -e openstack-heat-virtualenv-python-simplejson
rpm -e openstack-heat-virtualenv-python-six
rpm -e openstack-heat-virtualenv-python-argparse
rpm -e openstack-heat-virtualenv-python-pbr
rpm -e openstack-heat-virtualenv

    
cd %{_builddir}/opt
for FILE in `find . -name *.pyc`
do
    rm -f ${FILE}
done

for FILE in `find . -name *.pyo`
do
    rm -f ${FILE}
done


deactivate
##################################################################################################
esc_venv=$(echo $venv | sed 's/[\/&]/\\&/g')
pattern="s/#\!${esc_venv}\/bin\/python/#\!\/usr\/bin\/env python\nimport os; activate_this=os.environ.get('VIRTUAL_ENV') + '\/bin\/activate_this.py'\; execfile\(activate_this, dict\(__file__=activate_this\)\); del os, activate_this/g"
find $venv -type f -name "*.pyc" -exec rm -f {} \;
find $venv -type f -exec sed -i "$pattern" {} \;
sed -i "s/${esc_venv}/%CHANGE_VIRTUALENV_PATH%/g" $venv/bin/* || true
# recrete symlink with relative target
cd $venv
rm -f lib64
ln -s lib lib64
##################################################################################################

# 
%install
cp -r %{_builddir}/opt %{buildroot}/




%post

# determine where package installed, need to know prefix
# RPM ca
real_prefix=`rpm -q --queryformat "%{instprefixes}\n" %{name} | tail -n1`
#echo  ${real_prefix}

esc_real_venv=$(echo "${real_prefix}" | sed 's/[\/&]/\\&/g')
# replace patters to real prefix where package installed
sed -i "s/%CHANGE_VIRTUALENV_PATH%/${esc_real_venv}/g" ${real_prefix}/bin/*


%files
%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 13 2013 Max Mazur mmaxur@mirantis.com
- python-cinderclient for heat into virtualenv. Initial spec created.
