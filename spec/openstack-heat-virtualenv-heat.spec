%global release_name grizzly
%global release_letter master
%global milestone 0
%global full_release heat-%{version}.%{release_letter}

%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

Name:           openstack-heat
Summary:        OpenStack Orchestration (heat)
Version:        2013.3
Release:        0.3%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            http://www.openstack.org
Source0:        heat-%{version}.%{release_letter}.tar.gz
Source1:        heat.logrotate
Source2:        openstack-heat-api.init
Source3:        openstack-heat-api-cfn.init
Source4:        openstack-heat-engine.init
Source5:        openstack-heat-api-cloudwatch.init
Obsoletes:      heat < 7-9
Provides:       heat


Source6:        openstack-heat-virtualenv-0.1-1.el6.x86_64.rpm
Source7:        openstack-heat-virtualenv-python-netaddr-0.7.10-1.el6.noarch.rpm
Source8:        openstack-heat-virtualenv-python-pytz-2013b-1.el6.noarch.rpm
Source9:        openstack-heat-virtualenv-python-pyparsing-1.5.7-1.el6.noarch.rpm
Source10:       openstack-heat-virtualenv-python-amqp-1.0.13-1.el6.noarch.rpm
Source11:       openstack-heat-virtualenv-python-anyjson-0.3.3-1.el6.noarch.rpm
Source12:       openstack-heat-virtualenv-python-argparse-1.2.1-1.el6.noarch.rpm
Source13:       openstack-heat-virtualenv-python-babel-1.3-1.el6.noarch.rpm
Source14:       openstack-heat-virtualenv-python-prettytable-0.7.2-1.el6.noarch.rpm
Source15:       openstack-heat-virtualenv-python-cmd2-0.6.5.1-1.el6.noarch.rpm
Source16:       openstack-heat-virtualenv-python-cliff-1.4.2-1.el6.noarch.rpm
Source17:       openstack-heat-virtualenv-python-d2to1-0.2.10-1.el6.noarch.rpm
Source18:       openstack-heat-virtualenv-python-decorator-3.4.0-1.el6.noarch.rpm
Source19:       openstack-heat-virtualenv-python-greenlet-0.4.1-1.el6.noarch.rpm
Source20:       openstack-heat-virtualenv-python-eventlet-0.13.0-1.el6.noarch.rpm
Source21:       openstack-heat-virtualenv-python-httplib2-0.8-1.el6.noarch.rpm
Source22:       openstack-heat-virtualenv-python-importlib-1.0.2-1.el6.noarch.rpm
Source23:       openstack-heat-virtualenv-python-iso8601-0.1.4-1.el6.noarch.rpm
Source24:       openstack-heat-virtualenv-python-jinja2-2.7.1-1.el6.noarch.rpm
Source25:       openstack-heat-virtualenv-python-jsonschema-1.3.0-1.el6.noarch.rpm
Source26:       openstack-heat-virtualenv-python-repoze-lru-0.6-1.el6.noarch.rpm
Source27:       openstack-heat-virtualenv-python-lxml-3.2.3-1.el6.noarch.rpm
Source28:       openstack-heat-virtualenv-python-markupsafe-0.18-1.el6.noarch.rpm
Source29:       openstack-heat-virtualenv-python-mako-0.8.1-1.el6.noarch.rpm
Source30:       openstack-heat-virtualenv-python-ordereddict-1.1-1.el6.noarch.rpm
Source31:       openstack-heat-virtualenv-python-oslo-config-1.1.1-1.el6.noarch.rpm
Source32:       openstack-heat-virtualenv-python-paramiko-1.11.0-1.el6.noarch.rpm
Source33:       openstack-heat-virtualenv-python-pastedeploy-1.5.0-1.el6.noarch.rpm
Source34:       openstack-heat-virtualenv-python-pbr-0.5.21-1.el6.noarch.rpm
Source35:       openstack-heat-virtualenv-python-pycrypto-2.6-1.el6.noarch.rpm
Source36:       openstack-heat-virtualenv-python-pyyaml-3.10-1.el6.noarch.rpm
Source37:       openstack-heat-virtualenv-python-routes-1.13-1.el6.noarch.rpm
Source38:       openstack-heat-virtualenv-python-requests-1.2.2-1.el6.noarch.rpm
Source39:       openstack-heat-virtualenv-python-simplejson-3.3.0-1.el6.noarch.rpm
Source40:       openstack-heat-virtualenv-python-six-1.3.0-1.el6.noarch.rpm
Source41:       openstack-heat-virtualenv-python-sqlalchemy-0.7.10-1.el6.noarch.rpm
Source42:       openstack-heat-virtualenv-python-tempita-0.5.1-1.el6.noarch.rpm
Source43:       openstack-heat-virtualenv-python-webob-1.2.3-1.el6.noarch.rpm
Source44:       openstack-heat-virtualenv-python-werkzeug-0.9.3-1.el6.noarch.rpm
Source45:       openstack-heat-virtualenv-python-kombu-2.5.12-1.el6.noarch.rpm
Source46:       openstack-heat-virtualenv-python-flask-0.9-1.el6.noarch.rpm
Source47:       openstack-heat-virtualenv-python-alembic-0.6.0-1.el6.noarch.rpm
Source48:       openstack-heat-virtualenv-python-cinderclient-1.0.5-1.el6.noarch.rpm
Source49:       openstack-heat-virtualenv-python-keystoneclient-0.3.1-1.el6.noarch.rpm
Source50:       openstack-heat-virtualenv-python-ceilometerclient-1.0.3-1.el6.noarch.rpm
Source51:       openstack-heat-virtualenv-python-swiftclient-1.5.0-1.el6.noarch.rpm
Source52:       openstack-heat-virtualenv-python-novaclient-2.14.1-1.el6.noarch.rpm
Source53:       openstack-heat-virtualenv-python-neutronclient-2.2.6-1.el6.noarch.rpm
Source54:       openstack-heat-virtualenv-python-sqlalchemy-migrate-0.7.2-1.el6.noarch.rpm 



BuildArch:     noarch
 
BuildRequires: python-virtualenv
Requires: openstack-heat-virtualenv-0.1-1.el6.x86_64.rpm
Requires: openstack-heat-virtualenv-python-pytz-2013b-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-alembic-0.6.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-amqp-1.0.13-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-anyjson-0.3.3-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-argparse-1.2.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-babel-1.3-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-cinderclient-1.0.5-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-cliff-1.4.2-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-cmd2-0.6.5.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-d2to1-0.2.10-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-decorator-3.4.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-eventlet-0.13.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-flask-0.9-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-greenlet-0.4.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-httplib2-0.8-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-importlib-1.0.2-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-iso8601-0.1.4-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-jinja2-2.7.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-jsonschema-1.3.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-keystoneclient-0.2.5-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-keystoneclient-0.3.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-lxml-3.2.3-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-mako-0.8.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-markupsafe-0.18-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-netaddr-0.7.10-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-ordereddict-1.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-oslo-config-1.1.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-paramiko-1.11.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-pastedeploy-1.5.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-pbr-0.5.21-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-prettytable-0.7.2-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-pycrypto-2.6-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-pyparsing-1.5.7-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-pyyaml-3.10-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-repoze-lru-0.6-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-requests-1.2.2-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-routes-1.13-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-simplejson-3.3.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-six-1.3.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-sqlalchemy-0.7.10-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-tempita-0.5.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-webob-1.2.3-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-werkzeug-0.9.3-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-kombu-2.5.12-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-ceilometerclient-1.0.3-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-swiftclient-1.5.0-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-novaclient-2.14.1-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-neutronclient-2.2.6-1.el6.noarch.rpm
Requires: openstack-heat-virtualenv-python-sqlalchemy-migrate-0.7.2-1.el6.noarch.rpm

AutoReqProv: no

Prefix:         /opt/openstack-heat
%global debug_package %{nil}
#%define _binaries_in_noarch_packages_terminate_build   0


%description
heat in virtual environment for openstack-heat


%build

rm -rf  %{_builddir}%{prefix}

export PYTHONPATH=$PWD:${PYTHONPATH}
venv=%{_builddir}%{prefix}

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE6
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE7
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE8
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE9

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE10
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE11
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE12
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE13
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE14
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE15
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE16
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE17
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE18
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE19

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE20
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE21
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE22
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE23
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE24
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE25
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE26
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE27
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE28
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE29
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE30


rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE31
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE32
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE33
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE34
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE35
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE36
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE37
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE38
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE39
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE40


rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE41
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE42
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE43
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE44
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE45
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE46
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE47
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE48
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE49
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE50

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE51
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE52
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE53
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE54



source $venv/bin/activate

$venv/bin/pip install %SOURCE0


# Cleanup    
rpm -e openstack-heat-virtualenv-python-flask \
 openstack-heat-virtualenv-python-werkzeug \
 openstack-heat-virtualenv-python-webob \
 openstack-heat-virtualenv-python-tempita \
 openstack-heat-virtualenv-python-swiftclient \
 openstack-heat-virtualenv-python-sqlalchemy \
 openstack-heat-virtualenv-python-sqlalchemy-migrate  \
 openstack-heat-virtualenv-python-six \
 openstack-heat-virtualenv-python-simplejson \
 openstack-heat-virtualenv-python-routes \
 openstack-heat-virtualenv-python-requests  \
 openstack-heat-virtualenv-python-repoze-lru  \
 openstack-heat-virtualenv-python-pyyaml \
 openstack-heat-virtualenv-python-pytz \
 openstack-heat-virtualenv-python-pyparsing \
 openstack-heat-virtualenv-python-pycrypto \
 openstack-heat-virtualenv-python-prettytable \
 openstack-heat-virtualenv-python-pbr \
 openstack-heat-virtualenv-python-pastedeploy \
 openstack-heat-virtualenv-python-paramiko \
 openstack-heat-virtualenv-python-oslo-config \
 openstack-heat-virtualenv-python-ordereddict \
 openstack-heat-virtualenv-python-novaclient \
 openstack-heat-virtualenv-python-neutronclient \
 openstack-heat-virtualenv-python-netaddr \
 openstack-heat-virtualenv-python-markupsafe \
 openstack-heat-virtualenv-python-mako \
 openstack-heat-virtualenv-python-lxml \
 openstack-heat-virtualenv-python-kombu \
 openstack-heat-virtualenv-python-keystoneclient \
 openstack-heat-virtualenv-python-jsonschema \
 openstack-heat-virtualenv-python-jinja2 \
 openstack-heat-virtualenv-python-iso8601 \
 openstack-heat-virtualenv-python-importlib \
 openstack-heat-virtualenv-python-httplib2 \
 openstack-heat-virtualenv-python-greenlet \
 openstack-heat-virtualenv-python-eventlet \
 openstack-heat-virtualenv-python-decorator \
 openstack-heat-virtualenv-python-d2to1 \
 openstack-heat-virtualenv-python-cmd2 \
 openstack-heat-virtualenv-python-cliff \
 openstack-heat-virtualenv-python-cinderclient \
 openstack-heat-virtualenv-python-ceilometerclient \
 openstack-heat-virtualenv-python-babel \
 openstack-heat-virtualenv-python-argparse \
 openstack-heat-virtualenv-python-anyjson \
 openstack-heat-virtualenv-python-amqp \
 openstack-heat-virtualenv-python-alembic \
 openstack-heat-virtualenv
    
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
#HOME=%{_sharedstatedir}/heat
#install -d -m 700 %{buildroot}$HOME
# TODO: os_admin_username/password/tenant_name
#SAMPLE=%{buildroot}%{prefix}%{_datadir}/heat/heat.conf.sample
#SAMPLE=%{_builddir}%{prefix}/share/heat/heat.conf.sample
#CONF=%{_builddir}%{_sysconfdir}/heat/heat.conf

#install -d -m 755 $(dirname $CONF)
#install -D -m 640 $SAMPLE $CONF



mkdir -p %{buildroot}/var/log/heat
mkdir -p %{buildroot}/var/lib/heat
mkdir -p %{buildroot}/var/run/heat

mkdir -p %{buildroot}/etc/init.d
#cp %SOURCE28 %{buildroot}/etc/init.d/

cp -r %{_builddir}/opt %{buildroot}/
cp -r %{_builddir}/etc %{buildroot}/




%post

# determine where package installed, need to know prefix
# RPM ca
real_prefix=`rpm -q --queryformat "%{instprefixes}\n" %{name} | tail -n1`
#echo  ${real_prefix}

esc_real_venv=$(echo "${real_prefix}" | sed 's/[\/&]/\\&/g')
# replace patters to real prefix where package installed
sed -i "s/%CHANGE_VIRTUALENV_PATH%/${esc_real_venv}/g" ${real_prefix}/bin/*


EOF




%files
%dir %{_sysconfdir}/heat
# Note: this file is not readable because it holds auth credentials
%config(noreplace) %attr(-, root, heat) %{_sysconfdir}/heat/heat.conf
%config(noreplace) %attr(-, root, heat) /etc/heat/heat.conf
%dir %attr(-, heat, heat) %{_sharedstatedir}/heat

%dir %attr(-, heat, heat) /var/log/heat
%dir %attr(-, heat, heat) /var/lib/heat
%dir %attr(-, heat, heat) /var/run/heat
%config /etc/init.d/*
%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 13 2013 Max Mazur mmaxur@mirantis.com
- heat for heat into virtualenv. Initial spec created.
