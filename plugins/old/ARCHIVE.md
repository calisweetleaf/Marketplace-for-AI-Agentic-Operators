# Archived Plugin Packages

This directory preserves legacy/provenance plugin packages. It is **not** an active marketplace or runtime plugin root.

## Current archive contents

- `Codex-Config-Topology/` — legacy Codex control-plane plugin package. The standalone `codex-config-topology` skill remains useful; this plugin is no longer in the active triad.
- `Parallax-Narthex/` — legacy meta-prompt/identity-drop package.
- `Parallax-Narthex/CPF-Plugin-Ariadne/` — legacy CPF/Ariadne package whose role is superseded by active `../Aeriadne/`.

## Active replacement

Use active package:

```text
/home/daeron/Repositories/Somnus-Intellligence-Stack/plugins/Aeriadne
```

Canonical active plugin id:

```text
aeriadne
```

Legacy aliases retained for search/provenance only:

```text
Ariadne
cpf-plugin-ariadne
CPF-Plugin-Ariadne
Parallax-Narthex
```

## Important scanner boundary

Archived packages must not advertise active runtime plugin marker directories directly under `plugins/old/`. Historical `.codex-plugin/` and `.claude-plugin/` marker directories are moved to:

```text
plugins/old/_archived-plugin-descriptors/
```

That keeps file provenance without letting recursive marketplace or plugin scans accidentally expose legacy/stale packages as installable active plugins.
