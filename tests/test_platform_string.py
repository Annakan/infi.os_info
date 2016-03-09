from infi import unittest
from infi.os_info import get_platform_string
from os import environ
from copy import  deepcopy

test_subjects = [
    dict(expected='linux-ubuntu-quantal-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.5.0-40-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '12.10', 'quantal')),
    dict(expected='linux-ubuntu-quantal-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.5.0-40-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '12.10', 'quantal')),
    dict(expected='linux-ubuntu-saucy-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.11.0-26-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='linux-ubuntu-saucy-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.11.0-26-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-saucy-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.11.0-13-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='linux-ubuntu-saucy-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.11.0-13-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='linux-ubuntu-saucy-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.11.0-26-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='linux-ubuntu-saucy-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.11.0-20-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-centos-4-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.9-89.EL', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '4.8', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.14.1.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.17.1.el6.iscsigw.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.14.1.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.14.1.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-ubuntu-lucid-x86', system='Linux', architecture=('32bit', 'ELF'), processor='', release='2.6.32-54-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '10.04', 'lucid')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.17.1.el6.iscsigw.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-redhat-5-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-100.26.2.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='linux-redhat-6-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.32-100.34.1.el6uek.i686', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '6.1', 'Santiago')),
    dict(expected='linux-ubuntu-lucid-x86', system='Linux', architecture=('32bit', 'ELF'), processor='', release='2.6.32-53-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '10.04', 'lucid')),
    dict(expected='linux-redhat-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.el7.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '7.0', 'Maipo')),
    dict(expected='linux-redhat-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.el7.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '7.0', 'Maipo')),
    dict(expected='linux-redhat-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.el7.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '7.0', 'Maipo')),
    dict(expected='linux-centos-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.el7.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS Linux', '7.0.1406', 'Core')),
    dict(expected='linux-centos-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.el7.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS Linux', '7.0.1406', 'Core')),
    dict(expected='linux-ubuntu-trusty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.13.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-redhat-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.6.3.el7.iscsigw.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '7.0', 'Maipo')),
    dict(expected='linux-redhat-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.6.3.el7.iscsigw.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '7.0', 'Maipo')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.29.2.1.el6.izbox.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.29.2.1.el6.izbox.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-ubuntu-trusty-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.13.0-35-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-centos-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.el7.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS Linux', '7.0.1406', 'Core')),
    dict(expected='linux-ubuntu-natty-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.38-16-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.04', 'natty')),
    dict(expected='linux-ubuntu-lucid-x86', system='Linux', architecture=('32bit', 'ELF'), processor='', release='2.6.32-57-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '10.04', 'lucid')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.17.1.el6.iscsigw.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-redhat-6-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.32-122.el6.i686', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '6.1', 'Santiago')),
    dict(expected='linux-ubuntu-lucid-x86', system='Linux', architecture=('32bit', 'ELF'), processor='', release='2.6.32-54-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '10.04', 'lucid')),
    dict(expected='linux-redhat-5-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.18-229.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='linux-redhat-6-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.32-122.el6.i686', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '6.1', 'Santiago')),
    dict(expected='linux-redhat-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-122.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '6.1', 'Santiago')),
    dict(expected='linux-redhat-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-122.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '6.1', 'Santiago')),
    dict(expected='linux-redhat-5-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.18-229.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='linux-redhat-5-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.18-229.el5PAE', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-oneiric-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2012Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-ubuntu-precise-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.2.0-56-generic-pae', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '12.04', 'precise')),
    dict(expected='linux-redhat-5-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.18-229.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='linux-ubuntu-precise-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.2.0-57-generic-pae', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '12.04', 'precise')),
    dict(expected='linux-ubuntu-precise-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.2.0-56-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '12.04', 'precise')),
    dict(expected='linux-ubuntu-oneiric-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-natty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.38-16-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.04', 'natty')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.14.1.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-ubuntu-oneiric-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.0.0-32-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.10', 'oneiric')),
    dict(expected='linux-ubuntu-saucy-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.11.0-13-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='linux-ubuntu-precise-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.2.0-56-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '12.04', 'precise')),
    dict(expected='linux-ubuntu-natty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.38-16-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.04', 'natty')),
    dict(expected='linux-ubuntu-precise-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.2.0-57-generic-pae', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '12.04', 'precise')),
    dict(expected='linux-ubuntu-trusty-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.13.0-24-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-centos-4-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.9-89.EL', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '4.8', 'Final')),
    dict(expected='linux-ubuntu-trusty-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.13.0-35-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.29.2.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-ubuntu-saucy-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.11.0-20-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '13.10', 'saucy')),
    dict(expected='windows-x86', system='Windows', architecture=('32bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.14.1.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-redhat-7-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.10.0-123.el7.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '7.0', 'Maipo')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.14.1.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-redhat-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-122.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '6.1', 'Santiago')),
    dict(expected='linux-redhat-5-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.18-229.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='linux-redhat-6-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.32-122.el6.i686', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '6.1', 'Santiago')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2012Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='linux-ubuntu-natty-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.38-16-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '11.04', 'natty')),
    dict(expected='linux-redhat-5-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.18-229.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.29.2.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.29.2.1.el6.izbox.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-ubuntu-trusty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.13.0-36-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-ubuntu-trusty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.13.0-36-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-ubuntu-trusty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.13.0-36-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-ubuntu-trusty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.13.0-36-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-centos-5-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.18-238.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '5.6', 'Final')),
    dict(expected='linux-centos-5-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.18-238.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '5.6', 'Final')),
    dict(expected='linux-centos-5-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.18-238.el5', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '5.6', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-358.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.4', 'Final')),
    dict(expected='linux-centos-6-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.32-71.el6.i686', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS Linux', '6.0', 'Final')),
    dict(expected='linux-centos-6-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.32-431.el6.x86_64', mac_ver=('', ('', '', ''), ''), linux_distribution=('CentOS', '6.5', 'Final')),
    dict(expected='linux-redhat-5-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.18-238.el5PAE', mac_ver=('', ('', '', ''), ''), linux_distribution=('Red Hat Enterprise Linux Server', '5.6', 'Tikanga')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2012Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2012Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x86', system='Windows', architecture=('32bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008ServerR2', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008ServerR2', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x86', system='Windows', architecture=('32bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2012Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x86', system='Windows', architecture=('32bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2012Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008ServerR2', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008ServerR2', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x86', system='Windows', architecture=('32bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008ServerR2', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x86', system='Windows', architecture=('32bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008ServerR2', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='linux-ubuntu-trusty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.13.0-35-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='linux-ubuntu-trusty-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.13.0-36-generic', mac_ver=('', ('', '', ''), ''), linux_distribution=('Ubuntu', '14.04', 'trusty')),
    dict(expected='windows-x64', system='Windows', architecture=('64bit', 'WindowsPE'), processor='', release='2008Server', mac_ver=('', ('', '', ''), ''), linux_distribution=('', '', '')),
    dict(expected='linux-suse-11-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.0.76-0.11-default', mac_ver=('', ('', '', ''), ''), linux_distribution=('SUSE Linux Enterprise Server ', '11', 'x86_64')),
    dict(expected='linux-suse-11-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='3.0.76-0.11-pae', mac_ver=('', ('', '', ''), ''), linux_distribution=('SUSE Linux Enterprise Server ', '11', 'i586')),
    dict(expected='linux-suse-10-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.16.60-0.85.1-default', mac_ver=('', ('', '', ''), ''), linux_distribution=('SUSE Linux Enterprise Server ', '10', 'x86_64')),
    dict(expected='linux-suse-10-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.16.60-0.85.1-bigsmp', mac_ver=('', ('', '', ''), ''), linux_distribution=('SUSE Linux Enterprise Server ', '10', 'i586')),
    dict(expected='linux-suse-10-x86', system='Linux', architecture=('32bit', 'ELF'), processor='i686', release='2.6.16.60-0.85.1-bigsmp', mac_ver=('', ('', '', ''), ''), linux_distribution=('SUSE Linux Enterprise Server ', '10', 'i586')),
    dict(expected='linux-suse-10-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='2.6.16.60-0.85.1-default', mac_ver=('', ('', '', ''), ''), linux_distribution=('SUSE Linux Enterprise Server ', '10', 'x86_64')),
    dict(expected='linux-suse-11-x64', system='Linux', architecture=('64bit', 'ELF'), processor='x86_64', release='3.0.76-0.11-default', mac_ver=('', ('', '', ''), ''), linux_distribution=('SUSE Linux Enterprise Server ', '11', 'x86_64')),
]


class FakePlatformMorule(object):
    """:param platform_module: a platform-like module that implements system, architecture, processor, release, mac_ver, linux_distribution"""

    def __init__(self, system, architecture, processor, release, mac_ver, linux_distribution):
        self.system = lambda: system
        self.architecture = lambda: architecture
        self.processor = lambda: processor
        self.release = lambda: release
        self.mac_ver = lambda: mac_ver
        self.linux_distribution = lambda: linux_distribution


class PlatformStringTestCase(unittest.TestCase):
    @unittest.parameters.iterate('test_subject', deepcopy(test_subjects))
    def test_platform_string(self, test_subject):
        expected = test_subject.pop('expected')
        self.assertEquals(expected, get_platform_string(FakePlatformMorule(**test_subject)))


class PlatformStringEnvironOverrideTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        environ['infi_dist_name'] = "xxx"
        environ['infi_dist_version'] = "yyy"

    @unittest.parameters.iterate('test_subject', deepcopy(test_subjects))
    def test_platform_environ_override_string(self, test_subject):
        expected = test_subject.pop('expected')
        expected_split = expected.split('-')
        if expected_split[0] == "linux":
            expected = "{}-xxx-yyy-{}".format(expected_split[0], expected_split[3])
        self.assertEquals(expected, get_platform_string(FakePlatformMorule(**test_subject)))

    @classmethod
    def tearDownClass(cls):
        del environ['infi_dist_name']
        del environ['infi_dist_version']
