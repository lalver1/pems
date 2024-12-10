# Getting started with development

!!! info

    This guide will take you through the process of getting the [`pems`](https://github.com/compilerla/pems) project running in
    your local development environment.

    `pems` uses [VS Code devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) to provide a
    platform-agnostic, standardized development environment.

    For more about why we use Dev Containers, check our Compiler's blog post:
    [_How to support a platform-agnostic engineering team with VS Code Dev Containers_](https://compiler.la/blog/2024/devcontainer-platform-agnostic-team).

## Prerequisites

This section describes the tooling you need to have installed and configured on your development machine before continuing.

### Git

Git is an open source version control system that we use in `pems` to track changes to the codebase over time. Many operating
systems come with Git already installed. Check if you have Git installed in a terminal with the following command:

```shell
git --version
```

If git is installed, the output should look similar to:

```console
$ git --version
git version 2.39.5
```

If Git is not installed, head to the [Git downloads page](https://git-scm.com/downloads) to get an installer for your operating
system.

### Docker and Docker Compose

Docker and Docker Compose (or just Compose) are key tools that allow for running the various services required for `pems`.

Confirm if you already have Docker installed, in a terminal:

```shell
docker --version
```

If Docker is installed, the output should look similar to:

```console
$ docker --version
Docker version 27.4.0, build bde2b89
```

And similarly to check if Compose is installed:

```shell
docker compose version
```

When Compose is installed, output will look similar to:

```console
$ docker compose version
Docker Compose version v2.31.0
```

There are different ways to acquire this software depending on your operating system. The simplest approach for Windows and
MacOS users is to install [Docker Desktop](https://docs.docker.com/desktop/).

??? warning "License requirements for Docker Desktop"

    Use of Docker Desktop is subject to [Docker's licensing terms](https://www.docker.com/legal/docker-subscription-service-agreement/).
    In particular, note that **Section 4.2** calls out government users specifically:

    > Government Entities shall not use Docker Desktop or access other Entitlements of the Service without purchasing a Subscription.

#### Windows

It is possible to run Docker and Compose on Windows without installing Docker Desktop. This involves using the [Windows Subsystem
for Linux v2 (WSL2)](https://learn.microsoft.com/en-us/windows/wsl/install#step-2-update-to-wsl-2), where Docker is configured
to run.

This article walks through this procedure in more detail:
[_How to run docker on Windows without Docker Desktop_](https://dev.to/_nicolas_louis_/how-to-run-docker-on-windows-without-docker-desktop-hik).

#### MacOS

With MacOS and [Homebrew](https://brew.sh/), installing Docker and Compose are as simple as:

```shell
brew install docker docker-compose colima
```

Once the install completes, start `colima` (an [open source container runtime](https://github.com/abiosoft/colima)):

```shell
brew services start colima
```

#### Linux

Docker CE (also known as Docker Engine) is how to run Docker and Compose on Linux. Docker provides an
[installation guide for Docker CE](https://docs.docker.com/engine/install/).

### VS Code and Dev Containers extension

VS Code is an open source Integrated Development Environment (IDE) from Microsoft. Check if you already have it installed:

```shell
code -v
```

If installed, output should look similar to:

```console
$ code -v
1.95.3
f1a4fb101478ce6ec82fe9627c43efbf9e98c813
x64
```

Otherwise, [download VS Code](https://code.visualstudio.com/download) for your operating system.

Once installed, open VS Code and enter `Ctrl`/`Cmd` + `P` to open the VS Code Quick Open pane. Then enter:

```console
ext install ms-vscode-remote.remote-containers
```

`ms-vscode-remote.remote-containers` is the Extension ID of the
[Dev Containers extension from Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
