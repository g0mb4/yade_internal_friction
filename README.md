# internal friction

YADE project

## usage

single run in visual mode (manual start/exit):

```bash
./run.sh
```

run N times in batch mode (no visual, automatic start/exit):

```bash
./run.sh N
```

run N times in batch-mode where the values of the friction angle come from *params.table*:

```bash
./run.sh N t
```

The output of the simulation (position of the highest particle) is appended to *data.csv*.

