# `pywes`

**Usage**:

```console
$ pywes [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `client`: Control the simulation client.
* `install-ngspice`: Install ngspice executable in the correct...
* `server`: Control the simulation server.

## `pywes client`

Control the simulation client.

**Usage**:

```console
$ pywes client [OPTIONS] COMMAND:[start|stop]
```

**Arguments**:

* `COMMAND:[start|stop]`: [required]

**Options**:

* `--help`: Show this message and exit.

## `pywes install-ngspice`

Install ngspice executable in the correct location.

**Usage**:

```console
$ pywes install-ngspice [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `pywes server`

Control the simulation server.

**Usage**:

```console
$ pywes server [OPTIONS] COMMAND:[start|stop]
```

**Arguments**:

* `COMMAND:[start|stop]`: [required]

**Options**:

* `--help`: Show this message and exit.
