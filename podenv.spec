# generated by cabal-rpm-2.1.0 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global githash 53e4455

%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

Name:           podenv
Version:        0.1.0.0
Release:        0.20211103
Summary:        A podman wrapper

License:        ASL 2.0
Url:            https://github.com/podenv/podenv
Source:         %{name}-%{version}.tar.gz

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-dhall-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-either-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-gitrev-devel
BuildRequires:  ghc-lens-family-core-devel
#BuildRequires:  ghc-lens-family-th-devel
#BuildRequires:  ghc-linux-capabilities-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-relude-devel
BuildRequires:  ghc-text-devel
#BuildRequires:  ghc-th-env-devel
BuildRequires:  ghc-typed-process-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  cabal-install > 1.18
# for missing dep 'lens-family-th':
BuildRequires:  ghc-template-haskell-devel
# End cabal-rpm deps
BuildRequires:  git-core
Requires:       podman

%description
Podenv provides a declarative interface to manage containerized application.
Using rootless containers, podenv let's you run applications seamlessly.


%prep
%setup -q


%build
# Begin cabal-rpm build:
cabal update
PODENV_COMMIT=%{githash} cabal build
# End cabal-rpm build


%install
mkdir -p %{buildroot}%{_bindir}
strip -s -o %{buildroot}%{_bindir}/podenv dist-newstyle/build/*/ghc-*/podenv-%{version}/x/podenv/build/podenv/podenv
# Begin cabal-rpm install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
# End cabal-rpm files


%changelog
* Wed Nov  3 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20211103
- update to 53e4455
- https://github.com/podenv/podenv/commits/main

* Tue Nov  2 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20211101
- update to b7e4c7a

* Mon Nov  1 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20211030
- update to c9eea03

* Tue Oct 26 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20211026
- update to 692682a

* Mon Oct 25 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20211025
- update to 5b1e758

* Mon Oct 18 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20211018
- update to d0f8b27
- short githash for snapshot should now appear in --version

* Mon Oct  4 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20211004
- update to a9c241a

* Thu Sep 23 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20210923.1
- update to 87838f7 tarball

* Thu Sep 23 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20210923
- update to be20ef4

* Wed Sep 22 2021 Jens Petersen <petersen@redhat.com> - 0.1.0.0-0.20210922
- initial packaging
