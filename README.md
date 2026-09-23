# J-job — separate projects, separate databases

Separate business ideas. They share a principal and nothing else: separate trees,
separate intake, separate dashboards, separate published artifacts. Nothing crosses between
them, by construction — `build.py` reads one project's directory at a time, and a `rel` edge
pointing outside its own project is dropped.

    model-validation/    independent external verification of quantitative models (Japan, HK, East Asia)
    data-signal/         scoping the trading value of a dataset for the people who own it
    game-ml/             applied machine learning for Japanese game companies
    tools/               intake, retirement, dashboard checks
    build.py             builds BOTH dashboards, one per project
    dashboard.template.html   shared template; the data decides which project it renders

Each project directory holds its own complete database:

    <project>/entities/{org,person,venue,artifact}/
    <project>/notes/
    <project>/tasks/
    <project>/streams/
    <project>/intake/        harvested pools (model-validation only, so far)
    <project>/dashboard.html generated — never edit by hand

## Working on it

    python3 build.py                   # rebuild both dashboards
    python3 tools/check_dashboard.py   # static-check them before publishing

See `SCHEMA.md` for the card fields and `INTAKE.md` for how companies enter a project.

## The rule that keeps it usable

Each dashboard opens on **Do next**: about three live (priority-1) tasks, in order, each
stating what it settles. Everything else is background for those decisions. A project with
fifteen priority-1 tasks is a reading list, not a plan, and `build.py` warns when it drifts.

## Current focus

`game-ml`, newest. `data-signal` is reduced to a time-boxed credential project after its
business case failed. `model-validation` is parked — its regulatory research and named target
lists stay valid, but nothing in it is live work.

Adding a project means adding a directory and an entry in `PROJECTS` in `build.py`. Nothing
else.
