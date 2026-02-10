# pgAdmin 4 Desktop - Arch Linux Package

Unofficial Arch Linux package for pgAdmin 4 Desktop built from source with Electron runtime.

## Description

This package builds pgAdmin 4 desktop application from official source code using the Electron runtime. Unlike the official pgAdmin packages, this builds everything from source and uses a native Electron wrapper.

## Installation

### From AUR

```bash
yay -S pgadmin4-desktop-native
# or
paru -S pgadmin4-desktop-native
```

### Manual Build

```bash
git clone https://github.com/IlyaP358/pgadmin4.git
cd pgadmin4
makepkg -si
```

## Features

- Built from official pgAdmin source code
- Native Electron desktop application
- Full Python virtual environment included
- Webpack-bundled web interface

## Requirements

- Python 3
- Node.js and npm
- Yarn package manager

## Usage

After installation, launch pgAdmin 4 from your application menu or run:

```bash
pgadmin4
```

## Package Structure

```
/opt/pgadmin4-native/
├── venv/              # Python virtual environment
├── web/               # Web application bundle
└── runtime/           # Electron runtime
    └── dev_config.json
```

## Building

The build process includes:
1. Creating Python virtual environment
2. Installing Python dependencies
3. Building web frontend with webpack
4. Installing Electron runtime
5. Packaging everything together

Build time: ~15-20 minutes

## License

PostgreSQL License (same as pgAdmin 4)

## Links

- [Official pgAdmin Website](https://www.pgadmin.org/)
- [pgAdmin GitHub](https://github.com/pgadmin-org/pgadmin4)
- [AUR Package](https://aur.archlinux.org/packages/pgadmin4-desktop-native)

## Maintainer

Illium - [GitHub](https://github.com/IlyaP358) - <illia.pukalov@teleinformatika.eu>
