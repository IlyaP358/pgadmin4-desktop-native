# Maintainer: Illium <illia.pukalov@teleinformatika.eu> https://github.com/IlyaP358

pkgname=pgadmin4-desktop-native
pkgver=9.12
pkgrel=1
pkgdesc="pgAdmin 4 desktop (Electron runtime) built from source"
arch=('x86_64')
url="https://www.pgadmin.org/"
license=('PostgreSQL')

depends=(
  'python'
)
makedepends=(
  'python'
  'nodejs'
  'npm'
  'yarn'
)

source=(
  "https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v${pkgver}/source/pgadmin4-${pkgver}.tar.gz"
  "pgadmin4.desktop"
  "pgadmin4-128x128.png"
)
sha256sums=('f72f5d688eed9f65d523046492ce868bcb4251c04f763cb6b834b13be0ad6744'
            '676447c4c91cb291f50a6ec219e2fd024a0eabdedeac2be5cebaa594bfc00595'
            '65414f475058a5cf6f784ccfdbedb812083d72f1fd98889525f68f08a148820f')

prepare() {
  cd "${srcdir}/pgadmin4-${pkgver}"
}

build() {
  cd "${srcdir}/pgadmin4-${pkgver}"

  # Delete packageManager from package.json to use system yarn
  sed -i '/"packageManager":/d' web/package.json
  sed -i '/"packageManager":/d' runtime/package.json

  # Step 1: Python venv

  _venvdir="${srcdir}/venv-build"
  python -m venv "${_venvdir}"
  "${_venvdir}/bin/pip" install --upgrade pip setuptools wheel
  "${_venvdir}/bin/pip" install -r requirements.txt

  # Step 2: Web frontend bundle
  cd "${srcdir}/pgadmin4-${pkgver}/web"
  yarn install
  yarn run bundle

  # Step 3: Electron runtime
  cd "${srcdir}/pgadmin4-${pkgver}/runtime"
  yarn install
}

package() {
  cd "${srcdir}/pgadmin4-${pkgver}"
  local _optdir="${pkgdir}/opt/pgadmin4-native"

  # Create directory structure
  mkdir -p "${_optdir}"

  # Copy venv
  cp -a "${srcdir}/venv-build" "${_optdir}/venv"

  # Copy web
  cp -a web "${_optdir}/web"

  # Copy runtime
  cp -a runtime "${_optdir}/runtime"

  # Create dev_config.json for overriding paths
  cat > "${_optdir}/runtime/dev_config.json" << 'EOF'
{
  "pythonPath": "/opt/pgadmin4-native/venv/bin/python3",
  "pgadminFile": "/opt/pgadmin4-native/web/pgAdmin4.py"
}
EOF

  # config_distro.py for Python part
  cat > "${_optdir}/web/config_distro.py" << 'EOF'
import os
APP_PATH = "/opt/pgadmin4-native"
VENV_PATH = os.path.join(APP_PATH, "venv")
PYTHON_EXECUTABLE = os.path.join(VENV_PATH, "bin", "python3")
WEBDIR = os.path.join(APP_PATH, "web")
EOF

  # Launcher script
  mkdir -p "${pkgdir}/usr/bin"
  cat > "${pkgdir}/usr/bin/pgadmin4" << 'LAUNCHER'
#!/bin/bash
set -e
cd /opt/pgadmin4-native/runtime
exec ./node_modules/.bin/electron .
LAUNCHER
  chmod 755 "${pkgdir}/usr/bin/pgadmin4"

  # Desktop file and icon
  install -Dm644 "${srcdir}/pgadmin4.desktop" \
    "${pkgdir}/usr/share/applications/pgadmin4.desktop"
  sed -i 's|^Exec=.*|Exec=/usr/bin/pgadmin4|' \
    "${pkgdir}/usr/share/applications/pgadmin4.desktop"
  install -Dm644 "${srcdir}/pgadmin4-128x128.png" \
    "${pkgdir}/usr/share/icons/hicolor/128x128/apps/pgadmin4.png"

  # Cleanup unnecessary files =]
  find "${_optdir}/venv" -name '__pycache__' -type d -exec rm -rf '{}' + 2>/dev/null || true
  find "${_optdir}/venv" -name '*.py[co]' -delete 2>/dev/null || true
  rm -rf "${_optdir}/venv/.cache" 2>/dev/null || true
  rm -rf "${_optdir}/web/node_modules/.cache" 2>/dev/null || true
  rm -rf "${_optdir}/runtime/node_modules/.cache" 2>/dev/null || true
}
