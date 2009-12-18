%define name iwlwifi-agn-ucode
%define version 1.0
%define release %mkrel 4

Summary: Intel Wireless WiFi Link microcode
Name: %{name}
Version: %{version}
Release: %{release}
License: Proprietary
Group: System/Kernel and hardware
Url: http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: iwlwifi-1000-ucode
Requires: iwlwifi-4965-ucode
Requires: iwlwifi-5000-ucode
Requires: iwlwifi-5150-ucode
Requires: iwlwifi-6000-ucode

%description
This package requires other packages containing microcode needed to
use the Intel Wireless WiFi Link devices.

%files
