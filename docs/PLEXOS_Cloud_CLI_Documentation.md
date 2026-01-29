# PLEXOS Cloud CLI Documentation

## 📚 Table of Contents

- [Root Command](#root-command)
- [auth](#auth)
  - [auth Principal](#auth-principal)
  - [auth get-token](#auth-get-token)
  - [auth login](#auth-login)
  - [auth logout](#auth-logout)
  - [auth status](#auth-status)
- [context](#context)
  - [context clear](#context-clear)
  - [context get](#context-get)
  - [context have](#context-have)
  - [context release-locks](#context-release-locks)
  - [context set](#context-set)
- [datahub](#datahub)
  - [datahub delete](#datahub-delete)
  - [datahub download](#datahub-download)
  - [datahub map-folder](#datahub-map-folder)
  - [datahub permission](#datahub-permission)
    - [datahub permission Do](#datahub-permission-do)
    - [datahub permission add-update](#datahub-permission-add-update)
    - [datahub permission delete](#datahub-permission-delete)
    - [datahub permission delete-rule](#datahub-permission-delete-rule)
    - [datahub permission list](#datahub-permission-list)
    - [datahub permission update-inheritParentPermission](#datahub-permission-update-inheritparentpermission)
  - [datahub resources.](#datahub-resources.)
  - [datahub revert](#datahub-revert)
  - [datahub search](#datahub-search)
  - [datahub share](#datahub-share)
    - [datahub share be](#datahub-share-be)
    - [datahub share create](#datahub-share-create)
    - [datahub share delete](#datahub-share-delete)
    - [datahub share list](#datahub-share-list)
  - [datahub symlink](#datahub-symlink)
    - [datahub symlink another](#datahub-symlink-another)
    - [datahub symlink create-cross-tenant](#datahub-symlink-create-cross-tenant)
    - [datahub symlink create-local](#datahub-symlink-create-local)
    - [datahub symlink delete](#datahub-symlink-delete)
    - [datahub symlink first](#datahub-symlink-first)
    - [datahub symlink list](#datahub-symlink-list)
    - [datahub symlink permissions.](#datahub-symlink-permissions.)
    - [datahub symlink the](#datahub-symlink-the)
  - [datahub sync](#datahub-sync)
  - [datahub undelete](#datahub-undelete)
  - [datahub unmap-folder](#datahub-unmap-folder)
  - [datahub upload](#datahub-upload)
- [environment](#environment)
  - [environment browser](#environment-browser)
  - [environment callback](#environment-callback)
  - [environment check-install-mapping](#environment-check-install-mapping)
  - [environment check-machine-identifiers](#environment-check-machine-identifiers)
  - [environment check-write-registry](#environment-check-write-registry)
  - [environment diagnostic-information](#environment-diagnostic-information)
  - [environment generate-web-link](#environment-generate-web-link)
  - [environment get](#environment-get)
  - [environment information](#environment-information)
  - [environment installation](#environment-installation)
  - [environment list-users](#environment-list-users)
  - [environment logging-path](#environment-logging-path)
  - [environment proxy-config](#environment-proxy-config)
  - [environment set](#environment-set)
  - [environment status](#environment-status)
- [input-data](#input-data)
  - [input-data db-to-xml](#input-data-db-to-xml)
  - [input-data update](#input-data-update)
  - [input-data xml-to-db](#input-data-xml-to-db)
- [insights](#insights)
  - [insights get-machine-recommendation](#insights-get-machine-recommendation)
- [intelligence](#intelligence)
- [licensing](#licensing)
  - [licensing download](#licensing-download)
  - [licensing download-aurora](#licensing-download-aurora)
  - [licensing refresh](#licensing-refresh)
- [log](#log)
  - [log parse](#log-parse)
- [simulation](#simulation)
  - [simulation Subcommands](#simulation-subcommands)
  - [simulation build-request-from-previous](#simulation-build-request-from-previous)
  - [simulation cancel](#simulation-cancel)
  - [simulation capability](#simulation-capability)
    - [simulation capability list](#simulation-capability-list)
  - [simulation different](#simulation-different)
  - [simulation enable](#simulation-enable)
  - [simulation engine](#simulation-engine)
    - [simulation engine list](#simulation-engine-list)
    - [simulation engine specified.](#simulation-engine-specified.)
    - [simulation engine upload](#simulation-engine-upload)
  - [simulation enqueue](#simulation-enqueue)
    - [simulation enqueue Command](#simulation-enqueue-command)
    - [simulation enqueue access](#simulation-enqueue-access)
    - [simulation enqueue allows](#simulation-enqueue-allows)
    - [simulation enqueue arguments](#simulation-enqueue-arguments)
    - [simulation enqueue build](#simulation-enqueue-build)
    - [simulation enqueue change.](#simulation-enqueue-change.)
    - [simulation enqueue chronological-split](#simulation-enqueue-chronological-split)
    - [simulation enqueue custom-plexos](#simulation-enqueue-custom-plexos)
    - [simulation enqueue gurobi](#simulation-enqueue-gurobi)
    - [simulation enqueue in](#simulation-enqueue-in)
    - [simulation enqueue monte-carlo](#simulation-enqueue-monte-carlo)
    - [simulation enqueue responses](#simulation-enqueue-responses)
    - [simulation enqueue simulation.](#simulation-enqueue-simulation.)
    - [simulation enqueue so](#simulation-enqueue-so)
    - [simulation enqueue standard](#simulation-enqueue-standard)
    - [simulation enqueue stochastic](#simulation-enqueue-stochastic)
    - [simulation enqueue subject](#simulation-enqueue-subject)
    - [simulation enqueue using](#simulation-enqueue-using)
  - [simulation in](#simulation-in)
  - [simulation list](#simulation-list)
  - [simulation monitor](#simulation-monitor)
  - [simulation progress](#simulation-progress)
  - [simulation run-group](#simulation-run-group)
  - [simulation simulation](#simulation-simulation)
- [solution](#solution)
  - [solution archive](#solution-archive)
  - [solution bi](#solution-bi)
    - [solution bi based](#solution-bi-based)
    - [solution bi delete](#solution-bi-delete)
    - [solution bi filtered](#solution-bi-filtered)
    - [solution bi list](#solution-bi-list)
    - [solution bi publish](#solution-bi-publish)
    - [solution bi status](#solution-bi-status)
  - [solution convert](#solution-convert)
    - [solution convert Objectives,](#solution-convert-objectives,)
    - [solution convert condense-file](#solution-convert-condense-file)
    - [solution convert database](#solution-convert-database)
    - [solution convert hybrid-to-parquet](#solution-convert-hybrid-to-parquet)
    - [solution convert of](#solution-convert-of)
    - [solution convert period](#solution-convert-period)
    - [solution convert zip-to-hybrid](#solution-convert-zip-to-hybrid)
    - [solution convert zip-to-parquet](#solution-convert-zip-to-parquet)
  - [solution delete](#solution-delete)
  - [solution files](#solution-files)
    - [solution files download](#solution-files-download)
    - [solution files list](#solution-files-list)
    - [solution files list-types](#solution-files-list-types)
  - [solution latest-id](#solution-latest-id)
  - [solution list](#solution-list)
  - [solution list-reports](#solution-list-reports)
  - [solution model](#solution-model)
  - [solution query](#solution-query)
    - [solution query configure-views](#solution-query-configure-views)
    - [solution query model](#solution-query-model)
  - [solution solution-report-upload](#solution-solution-report-upload)
  - [solution solution-reports](#solution-solution-reports)
  - [solution solution-stitching](#solution-solution-stitching)
  - [solution the](#solution-the)
  - [solution unarchive](#solution-unarchive)
  - [solution undone.)](#solution-undone.))
  - [solution view](#solution-view)
    - [solution view for](#solution-view-for)
    - [solution view get-downloadable-report-details](#solution-view-get-downloadable-report-details)
    - [solution view get-report-data](#solution-view-get-report-data)
    - [solution view list](#solution-view-list)
    - [solution view publish](#solution-view-publish)
    - [solution view report](#solution-view-report)
  - [solution with](#solution-with)
- [study](#study)
  - [study archive](#study-archive)
  - [study changeset](#study-changeset)
    - [study changeset are](#study-changeset-are)
    - [study changeset building](#study-changeset-building)
    - [study changeset download](#study-changeset-download)
    - [study changeset get-latest](#study-changeset-get-latest)
    - [study changeset get-latest-local](#study-changeset-get-latest-local)
    - [study changeset get-status](#study-changeset-get-status)
    - [study changeset get-urls](#study-changeset-get-urls)
    - [study changeset list](#study-changeset-list)
    - [study changeset list-local](#study-changeset-list-local)
    - [study changeset pull](#study-changeset-pull)
    - [study changeset push](#study-changeset-push)
    - [study changeset study's](#study-changeset-study's)
    - [study changeset tracked](#study-changeset-tracked)
    - [study changeset using](#study-changeset-using)
  - [study clone](#study-clone)
  - [study create](#study-create)
  - [study data](#study-data)
  - [study delete](#study-delete)
  - [study delete-local](#study-delete-local)
  - [study find](#study-find)
  - [study grant-user-access](#study-grant-user-access)
  - [study list](#study-list)
  - [study list-local](#study-list-local)
  - [study list-local-studyIDs](#study-list-local-studyids)
  - [study local](#study-local)
  - [study permanent](#study-permanent)
  - [study repair-local](#study-repair-local)
  - [study reset](#study-reset)
  - [study settings](#study-settings)
    - [study settings add-configurations](#study-settings-add-configurations)
    - [study settings create](#study-settings-create)
    - [study settings delete](#study-settings-delete)
    - [study settings list](#study-settings-list)
  - [study stats](#study-stats)
    - [study stats geocoded-objects](#study-stats-geocoded-objects)
  - [study unarchive](#study-unarchive)
  - [study validate](#study-validate)
- [tool](#tool)
  - [tool install](#tool-install)
  - [tool list](#tool-list)
  - [tool run](#tool-run)
  - [tool vscode](#tool-vscode)
- [upgrade](#upgrade)
  - [upgrade check](#upgrade-check)
  - [upgrade install](#upgrade-install)
- [users](#users)
  - [users create](#users-create)
  - [users downloadtemplate](#users-downloadtemplate)

---


*Generated on: 2025-08-30 09:53:29*
*CLI Version: Unknown*

---

## Root Command

### Help Output

```
CloudCLI.CloudCliApp

PLEXOS Cloud CLI

Usage: plexos-cloud [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  auth               Commands for handling cloud authorization
  context            Commands dealing with the local user context
  datahub            Manage datahub resources
  environment        Commands dealing with the configured cloud environment
  input-data         Manage input data
  insights           Commands dealing with simulation insights
  intelligence       Commands dealing with PLEXOS Intelligence
  licensing          Manage licensing
  log                Inspect Log files
  simulation         Manage simulations
  solution           Manage solutions
  study              Manage studies
  tool               Manage tools
  upgrade            Manage upgrades of CLI
  users              Manage users

Run 'plexos-cloud [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`auth`](#auth)
- [`context`](#context)
- [`datahub`](#datahub)
- [`environment`](#environment)
- [`input-data`](#input-data)
- [`insights`](#insights)
- [`intelligence`](#intelligence)
- [`licensing`](#licensing)
- [`log`](#log)
- [`simulation`](#simulation)
- [`solution`](#solution)
- [`study`](#study)
- [`tool`](#tool)
- [`upgrade`](#upgrade)
- [`users`](#users)

---

## `plexos-cloud auth`

**Command Path:** `plexos-cloud → auth`

### Help Output

```
CloudCLI.Commands.Authentication.AuthorizeCommand

Commands for handling cloud authorization

Usage: plexos-cloud auth [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  get-token          get current access token
  login              Login to PLEXOS Cloud, using either SSO or Service
                     Principal
  logout             Log out the current user and clear cached credentials
  status             Prints auth and environment summary

Run 'auth [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`Principal`](#auth-principal)
- [`get-token`](#auth-get-token)
- [`login`](#auth-login)
- [`logout`](#auth-logout)
- [`status`](#auth-status)

---

## `plexos-cloud context`

**Command Path:** `plexos-cloud → context`

### Help Output

```
CloudCLI.Commands.UserContext.UserContextCommand

Commands dealing with the local user context

Usage: plexos-cloud context [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  clear              Clears out the current user context
  get                Displays the current user context
  release-locks      Releases any resource locks that a previous instance may
                     have left due to errors
  set                Sets the current user context

Run 'context [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`clear`](#context-clear)
- [`get`](#context-get)
- [`have`](#context-have)
- [`release-locks`](#context-release-locks)
- [`set`](#context-set)

---

## `plexos-cloud datahub`

**Command Path:** `plexos-cloud → datahub`

### Help Output

```
CloudCLI.Commands.Datahub.DatahubCommand

Manage datahub resources

Usage: plexos-cloud datahub [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  delete             Deletes files on Datahub
  download           Downloads requested resources from datahub.
  map-folder         Set the mapping in between local and remote folders
  permission         Manage permissions on datahub
  revert             Reverts a file back to a specific version.
  search             Searches datahub via a list of patterns and returns found
                     resources.
  share              Manage sharing on datahub
  symlink            Manage symlinks on datahub
  sync               Sync's local folders with Datahub folders.
  undelete           Un-deletes files on Datahub
  unmap-folder       Unmap a local folder from a remote folder
  upload             Upload local files to datahub

Run 'datahub [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`delete`](#datahub-delete)
- [`download`](#datahub-download)
- [`map-folder`](#datahub-map-folder)
- [`permission`](#datahub-permission)
- [`resources.`](#datahub-resources.)
- [`revert`](#datahub-revert)
- [`search`](#datahub-search)
- [`share`](#datahub-share)
- [`symlink`](#datahub-symlink)
- [`sync`](#datahub-sync)
- [`undelete`](#datahub-undelete)
- [`unmap-folder`](#datahub-unmap-folder)
- [`upload`](#datahub-upload)

---

## `plexos-cloud environment`

**Command Path:** `plexos-cloud → environment`

### Help Output

```
CloudCLI.Commands.Environment.UserEnvironmentCommand

Commands dealing with the configured cloud environment

Usage: plexos-cloud environment [command] [options]

Options:
  -f|--format                Output format(json | csv | tsv | yaml | table |
                             none)
                             Allowed values are: JSON, JSONL, CSV, None, Table,
                             TSV, YAML.
                             Default value is: JSON.
  -q|--quiet                 Turns off verbose messages from app
  -aut|--automation          Turns on developer friendly structured response
                             messages from app
                             Allowed values are: None, PythonSDK.
  -?|-h|--help               Show help information.

Commands:
  check-install-mapping      Checks the mapping of the Cloud Toolkit
                             installation path
  check-machine-identifiers  Checks ability to read machine identifying
                             information for licensing purposes
  check-write-registry       Checks ability to write registry values for
                             callback
  diagnostic-information     Get the diagnostic information
  generate-web-link          Generates a Plexos Cloud Web Url to view in a
                             browser
  get                        Displays the current configured cloud environment
  list-users                 Get user details for tenant
  logging-path               Displays the folder path where log files are saved
  proxy-config               Displays proxy configuration
  set                        Sets the current configured cloud environment
  status                     Displays environment statuses

Run 'environment [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`browser`](#environment-browser)
- [`callback`](#environment-callback)
- [`check-install-mapping`](#environment-check-install-mapping)
- [`check-machine-identifiers`](#environment-check-machine-identifiers)
- [`check-write-registry`](#environment-check-write-registry)
- [`diagnostic-information`](#environment-diagnostic-information)
- [`generate-web-link`](#environment-generate-web-link)
- [`get`](#environment-get)
- [`information`](#environment-information)
- [`installation`](#environment-installation)
- [`list-users`](#environment-list-users)
- [`logging-path`](#environment-logging-path)
- [`proxy-config`](#environment-proxy-config)
- [`set`](#environment-set)
- [`status`](#environment-status)

---

## `plexos-cloud input-data`

**Command Path:** `plexos-cloud → input-data`

### Help Output

```
CloudCLI.Commands.InputData.InputDataCommand

Manage input data

Usage: plexos-cloud input-data [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  db-to-xml          Convert SQLite database to XML
  update             Update items from json in input data
  xml-to-db          Convert XML to SQLite database

Run 'input-data [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`db-to-xml`](#input-data-db-to-xml)
- [`update`](#input-data-update)
- [`xml-to-db`](#input-data-xml-to-db)

---

## `plexos-cloud insights`

**Command Path:** `plexos-cloud → insights`

### Help Output

```
CloudCLI.Commands.Insights.InsightsCommand

Commands dealing with simulation insights

Usage: plexos-cloud insights [command] [options]

Options:
  -f|--format                 Output format(json | csv | tsv | yaml | table |
                              none)
                              Allowed values are: JSON, JSONL, CSV, None, Table,
                              TSV, YAML.
                              Default value is: JSON.
  -q|--quiet                  Turns off verbose messages from app
  -aut|--automation           Turns on developer friendly structured response
                              messages from app
                              Allowed values are: None, PythonSDK.
  -?|-h|--help                Show help information.

Commands:
  get-machine-recommendation  get machine recommendation for group of models

Run 'insights [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`get-machine-recommendation`](#insights-get-machine-recommendation)

---

## `plexos-cloud intelligence`

**Command Path:** `plexos-cloud → intelligence`

### Help Output

```
CloudCLI.Commands.Intelligence.IntelligenceCommand

Commands dealing with PLEXOS Intelligence

Usage: plexos-cloud intelligence [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud licensing`

**Command Path:** `plexos-cloud → licensing`

### Help Output

```
CloudCLI.Commands.Licensing.LicensingCommand

Manage licensing

Usage: plexos-cloud licensing [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  download           Download PLEXOS or Connect license from empty license file
  download-aurora    Download Aurora license from MachineID and MachineName
  refresh            Refresh CLI license manually

Run 'licensing [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`download`](#licensing-download)
- [`download-aurora`](#licensing-download-aurora)
- [`refresh`](#licensing-refresh)

---

## `plexos-cloud log`

**Command Path:** `plexos-cloud → log`

### Help Output

```
CloudCLI.Commands.Logs.LogCommand

Inspect Log files

Usage: plexos-cloud log [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  parse              Parse Simulation Log

Run 'log [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`parse`](#log-parse)

---

## `plexos-cloud simulation`

**Command Path:** `plexos-cloud → simulation`

### Help Output

```
CloudCLI.Commands.Simulation.SimulationCommand

Manage simulations

Usage: plexos-cloud simulation [command] [options]

Options:
  -f|--format                  Output format(json | csv | tsv | yaml | table |
                               none)
                               Allowed values are: JSON, JSONL, CSV, None,
                               Table, TSV, YAML.
                               Default value is: JSON.
  -q|--quiet                   Turns off verbose messages from app
  -aut|--automation            Turns on developer friendly structured response
                               messages from app
                               Allowed values are: None, PythonSDK.
  -?|-h|--help                 Show help information.

Commands:
  build-request-from-previous  build simulation request based on previously ran
                               simulation
  cancel                       Cancel Simulation request
  capability                   Manage capabilities
  engine                       Manage engines
  enqueue                      Using top-level command with --file option will
                               enable enqueuing simulations from a JSON file.
                               Subcommands (Early Access) manages enqueuing
                               different types of simulations
  list                         List simulations
  monitor                      Monitor Simulations while they are running, i.e.
                               in progress state
  progress                     Check Simulation progress
  run-group                    Runs the simulation group.

Run 'simulation [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`Subcommands`](#simulation-subcommands)
- [`build-request-from-previous`](#simulation-build-request-from-previous)
- [`cancel`](#simulation-cancel)
- [`capability`](#simulation-capability)
- [`different`](#simulation-different)
- [`enable`](#simulation-enable)
- [`engine`](#simulation-engine)
- [`enqueue`](#simulation-enqueue)
- [`in`](#simulation-in)
- [`list`](#simulation-list)
- [`monitor`](#simulation-monitor)
- [`progress`](#simulation-progress)
- [`run-group`](#simulation-run-group)
- [`simulation`](#simulation-simulation)

---

## `plexos-cloud solution`

**Command Path:** `plexos-cloud → solution`

### Help Output

```
CloudCLI.Commands.Solution.SolutionCommand

Manage solutions

Usage: plexos-cloud solution [command] [options]

Options:
  -f|--format             Output format(json | csv | tsv | yaml | table | none)
                          Allowed values are: JSON, JSONL, CSV, None, Table,
                          TSV, YAML.
                          Default value is: JSON.
  -q|--quiet              Turns off verbose messages from app
  -aut|--automation       Turns on developer friendly structured response
                          messages from app
                          Allowed values are: None, PythonSDK.
  -?|-h|--help            Show help information.

Commands:
  archive                 This command will archive all solutions associated
                          with the execution.
  bi                      Manage Bi
  convert                 Commands dealing with converting solution databases
  delete                  This command will delete all solutions associated with
                          the given execution.(**this is permanent and cannot be
                          undone.)
  files                   Commands dealing with solution files
  latest-id               Gets most recent solution id created for a study &
                          model
  list                    List all solutions
  list-reports            List Solution Reports
  query                   Commands dealing with query solution data
  solution-report-upload  Uploads a solution report
  solution-reports        gets solution report data
  solution-stitching      stitch multiple solutions together to get new solution
  unarchive               This command will unarchive all solutions associated
                          with the given execution.
  view                    Manage views

Run 'solution [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`archive`](#solution-archive)
- [`bi`](#solution-bi)
- [`convert`](#solution-convert)
- [`delete`](#solution-delete)
- [`files`](#solution-files)
- [`latest-id`](#solution-latest-id)
- [`list`](#solution-list)
- [`list-reports`](#solution-list-reports)
- [`model`](#solution-model)
- [`query`](#solution-query)
- [`solution-report-upload`](#solution-solution-report-upload)
- [`solution-reports`](#solution-solution-reports)
- [`solution-stitching`](#solution-solution-stitching)
- [`the`](#solution-the)
- [`unarchive`](#solution-unarchive)
- [`undone.)`](#solution-undone.))
- [`view`](#solution-view)
- [`with`](#solution-with)
- [`with`](#solution-with)

---

## `plexos-cloud study`

**Command Path:** `plexos-cloud → study`

### Help Output

```
CloudCLI.Commands.Study.StudyCommand

Manage studies

Usage: plexos-cloud study [command] [options]

Options:
  -f|--format          Output format(json | csv | tsv | yaml | table | none)
                       Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                       YAML.
                       Default value is: JSON.
  -q|--quiet           Turns off verbose messages from app
  -aut|--automation    Turns on developer friendly structured response messages
                       from app
                       Allowed values are: None, PythonSDK.
  -?|-h|--help         Show help information.

Commands:
  archive              Archive the given Study
  changeset            Commands dealing with a study's changeset
  clone                Downloads and initializes a tracked study from the cloud
  create               Creates a study from input project file
  delete               Delete the given study from PLEXOS Cloud. (**this is
                       permanent and cannot be undone.)
  delete-local         Deletes local study files
  find                 Find the Study by name
  grant-user-access    Grants user access to a study
  list                 List studies
  list-local           List local studies that are tracked on the cloud
  list-local-studyIDs  Lists PLEXOS Cloud study IDs currently attached to a
                       local study directory
  repair-local         Attempts to repair the cloud sync of a local study when
                       data has been corrupted or study gets moved
  reset                Reset study on local to latest version on cloud
  settings             Manage studies settings
  stats                Commands dealing with a study's statistical information
  unarchive            Unarchive the given Study
  validate             Validate data for study creation

Run 'study [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`archive`](#study-archive)
- [`changeset`](#study-changeset)
- [`clone`](#study-clone)
- [`create`](#study-create)
- [`data`](#study-data)
- [`delete`](#study-delete)
- [`delete-local`](#study-delete-local)
- [`find`](#study-find)
- [`grant-user-access`](#study-grant-user-access)
- [`list`](#study-list)
- [`list-local`](#study-list-local)
- [`list-local-studyIDs`](#study-list-local-studyids)
- [`local`](#study-local)
- [`permanent`](#study-permanent)
- [`repair-local`](#study-repair-local)
- [`reset`](#study-reset)
- [`settings`](#study-settings)
- [`stats`](#study-stats)
- [`unarchive`](#study-unarchive)
- [`validate`](#study-validate)

---

## `plexos-cloud tool`

**Command Path:** `plexos-cloud → tool`

### Help Output

```
CloudCLI.Commands.Tool.ToolCommand

Manage tools

Usage: plexos-cloud tool [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  install            Install an available tool
  list               List available tools.
  run                Run an installed tool
  vscode             VSCode management

Run 'tool [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`install`](#tool-install)
- [`list`](#tool-list)
- [`run`](#tool-run)
- [`vscode`](#tool-vscode)

---

## `plexos-cloud upgrade`

**Command Path:** `plexos-cloud → upgrade`

### Help Output

```
CloudCLI.Commands.Upgrade.UpgradeCommand

Manage upgrades of CLI

Usage: plexos-cloud upgrade [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  check              Check for newer version
  install            Install upgrade if newer exists

Run 'upgrade [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`check`](#upgrade-check)
- [`install`](#upgrade-install)

---

## `plexos-cloud users`

**Command Path:** `plexos-cloud → users`

### Help Output

```
CloudCLI.Commands.Identity.UsersCommand

Manage users

Usage: plexos-cloud users [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  create             Beta: Create users in bulk from a csv file
  downloadtemplate   Beta: Download csv template for creating users

Run 'users [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`create`](#users-create)
- [`downloadtemplate`](#users-downloadtemplate)

---

## `plexos-cloud auth Principal`

**Command Path:** `plexos-cloud → auth → Principal`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'Principal'

```

---

## `plexos-cloud auth get-token`

**Command Path:** `plexos-cloud → auth → get-token`

### Help Output

```
CloudCLI.Commands.Authentication.GetTokenCommand

get current access token

Usage: plexos-cloud auth get-token [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud auth login`

**Command Path:** `plexos-cloud → auth → login`

### Help Output

```
CloudCLI.Commands.Authentication.LoginCommand

Login to PLEXOS Cloud, using either SSO or Service Principal

Usage: plexos-cloud auth login [options]

Options:
  -f|--format          Output format(json | csv | tsv | yaml | table | none)
                       Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                       YAML.
                       Default value is: JSON.
  -q|--quiet           Turns off verbose messages from app
  -aut|--automation    Turns on developer friendly structured response messages
                       from app
                       Allowed values are: None, PythonSDK.
  -c|--client-id       Service Principal Client Id
  -s|--client-secret   Service Principal Client Secret
  -t|--tenant-id       Service Principal Tenant Id
  --service-principal  Indicates that the credentials represent a service
                       principal
  -?|-h|--help         Show help information.


```

---

## `plexos-cloud auth logout`

**Command Path:** `plexos-cloud → auth → logout`

### Help Output

```
CloudCLI.Commands.Authentication.LogoutCommand

Log out the current user and clear cached credentials

Usage: plexos-cloud auth logout [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud auth status`

**Command Path:** `plexos-cloud → auth → status`

### Help Output

```
CloudCLI.Commands.Authentication.CheckAuthenticationStatusCommand

Prints auth and environment summary

Usage: plexos-cloud auth status [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud context clear`

**Command Path:** `plexos-cloud → context → clear`

### Help Output

```
CloudCLI.Commands.UserContext.ClearCurrentContextCommand

Clears out the current user context

Usage: plexos-cloud context clear [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --simulationId     Filter by the simulation ID
  --studyId          Filter by the study ID
  --executionId      Filter by the executionId ID
  --changesetId      Filter by the Changeset ID
  --solutionId       Filter by the solution ID
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud context get`

**Command Path:** `plexos-cloud → context → get`

### Help Output

```
CloudCLI.Commands.UserContext.GetCurrentContextCommand

Displays the current user context

Usage: plexos-cloud context get [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud context have`

**Command Path:** `plexos-cloud → context → have`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'have'

```

---

## `plexos-cloud context release-locks`

**Command Path:** `plexos-cloud → context → release-locks`

### Help Output

```
CloudCLI.Commands.UserContext.ReleaseApplicationLocksCommand

Releases any resource locks that a previous instance may have left due to errors

Usage: plexos-cloud context release-locks [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud context set`

**Command Path:** `plexos-cloud → context → set`

### Help Output

```
CloudCLI.Commands.UserContext.SetCurrentContextCommand

Sets the current user context

Usage: plexos-cloud context set [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --simulationId     Filter by the simulation ID
  --studyId          Filter by the study ID
  --executionId      Filter by the executionId ID
  --changesetId      Filter by the Changeset ID
  --solutionId       Filter by the solution ID
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub delete`

**Command Path:** `plexos-cloud → datahub → delete`

### Help Output

```
CloudCLI.Commands.Datahub.DeleteCommand

Deletes files on Datahub

Usage: plexos-cloud datahub delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --pattern          Specify globbing patterns that map to folders or files in
                     datahub for deletion (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub download`

**Command Path:** `plexos-cloud → datahub → download`

### Help Output

```
CloudCLI.Commands.Datahub.DownloadCommand

Downloads requested resources from datahub.

Usage: plexos-cloud datahub download [options]

Options:
  -f|--format             Output format(json | csv | tsv | yaml | table | none)
                          Allowed values are: JSON, JSONL, CSV, None, Table,
                          TSV, YAML.
                          Default value is: JSON.
  -q|--quiet              Turns off verbose messages from app
  -aut|--automation       Turns on developer friendly structured response
                          messages from app
                          Allowed values are: None, PythonSDK.
  -p|--pattern            Set filter patterns mapping to Datahub locations to
                          refine the selection of files to download - these can
                          be files or globbing patterns.
  -d|--outputDirectory    Directory to download Datahub files to.
  -v|--version            The version of the datahub files/folders you're
                          downloading. Optional - latest version is default.
  -s|--snapshotDate       The date of which to find what version of the file it
                          is. Optional - cannot be used with version.
  -m|--manifest           Path to a manifest file containing multiple paths,
                          rules, version specs, etc. Cannot be used with
                          pattern, version, or snapshot date arguments.
  --verify                Verify the content of the download against the
                          signature
  --whatif                Run a simulated download to make sure all files are
                          accessible and exist
  --create-metadata-file  Creates a CSV file containing metadata from the
                          downloaded files, can be used for verification
  -?|-h|--help            Show help information.
This command does not add Datahub mappings, it simply downloads files. Use "datahub map" and "datahub sync" instead.

```

---

## `plexos-cloud datahub map-folder`

**Command Path:** `plexos-cloud → datahub → map-folder`

### Help Output

```
CloudCLI.Commands.Datahub.Map.MapFolderCommand

Set the mapping in between local and remote folders

Usage: plexos-cloud datahub map-folder [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --local-folder     Set the local directory folder
  --remote-folder    Set the remote datahub folder
  --pattern          Set the filter patterns to refine the selection of files to
                     map
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub permission`

**Command Path:** `plexos-cloud → datahub → permission`

### Help Output

```
CloudCLI.Commands.Datahub.Permission.PermissionCommand

Manage permissions on datahub

Usage: plexos-cloud datahub permission [command] [options]

Options:
  -f|--format                     Output format(json | csv | tsv | yaml | table
                                  | none)
                                  Allowed values are: JSON, JSONL, CSV, None,
                                  Table, TSV, YAML.
                                  Default value is: JSON.
  -q|--quiet                      Turns off verbose messages from app
  -aut|--automation               Turns on developer friendly structured
                                  response messages from app
                                  Allowed values are: None, PythonSDK.
  -?|-h|--help                    Show help information.

Commands:
  add-update                      Add or update ACL permissions on datahub.
  delete                          Deletes a single permission on an ACL rule
  delete-rule                     Deletes the entire ACL rule
  list                            List all permissions
  update-inheritParentPermission  Flip the Inherit Parent permission for a rule.
                                  Do not use this command if you are not sure

Run 'permission [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`Do`](#datahub-permission-do)
- [`add-update`](#datahub-permission-add-update)
- [`delete`](#datahub-permission-delete)
- [`delete-rule`](#datahub-permission-delete-rule)
- [`list`](#datahub-permission-list)
- [`update-inheritParentPermission`](#datahub-permission-update-inheritparentpermission)

---

## `plexos-cloud datahub resources.`

**Command Path:** `plexos-cloud → datahub → resources.`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'resources.'

```

---

## `plexos-cloud datahub revert`

**Command Path:** `plexos-cloud → datahub → revert`

### Help Output

```
CloudCLI.Commands.Datahub.RevertCommand

Reverts a file back to a specific version.

Usage: plexos-cloud datahub revert [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --file             The local path to the file you want to revert
  -v|--version       The version to revert the file to.
  -s|--snapshotDate  The date of which to revert the file back to the version at
                     the time.
  --verify           Verify the content of the download against the signature
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub search`

**Command Path:** `plexos-cloud → datahub → search`

### Help Output

```
CloudCLI.Commands.Datahub.SearchCommand

Searches datahub via a list of patterns and returns found resources.

Usage: plexos-cloud datahub search [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -p|--pattern       Set glob filter patterns mapping to Datahub locations to
                     search.
  --include-deleted  Include soft deleted files that are matching the search
                     pattern
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub share`

**Command Path:** `plexos-cloud → datahub → share`

### Help Output

```
CloudCLI.Commands.Datahub.Share.ShareCommand

Manage sharing on datahub

Usage: plexos-cloud datahub share [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  create             Creates a share, which designates a Datahub folder that can
                     be shared and linked to by other tenants.
  delete             Deletes a share.
  list               Lists all shares in Datahub.

Run 'share [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`be`](#datahub-share-be)
- [`create`](#datahub-share-create)
- [`delete`](#datahub-share-delete)
- [`list`](#datahub-share-list)

---

## `plexos-cloud datahub symlink`

**Command Path:** `plexos-cloud → datahub → symlink`

### Help Output

```
CloudCLI.Commands.Datahub.Symlink.SymlinkCommand

Manage symlinks on datahub

Usage: plexos-cloud datahub symlink [command] [options]

Options:
  -f|--format          Output format(json | csv | tsv | yaml | table | none)
                       Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                       YAML.
                       Default value is: JSON.
  -q|--quiet           Turns off verbose messages from app
  -aut|--automation    Turns on developer friendly structured response messages
                       from app
                       Allowed values are: None, PythonSDK.
  -?|-h|--help         Show help information.

Commands:
  create-cross-tenant  Creates a symlink to a file or folder that is present in
                       another tenant in the same Environment. This requires to
                       first create a Share on the target tenant and set
                       permissions.
  create-local         Creates a symlink to a file or folder that is present in
                       the same Tenant.
  delete               Deletes a symlink.
  list                 Lists all symlinks in Datahub.

Run 'symlink [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`another`](#datahub-symlink-another)
- [`create-cross-tenant`](#datahub-symlink-create-cross-tenant)
- [`create-local`](#datahub-symlink-create-local)
- [`delete`](#datahub-symlink-delete)
- [`first`](#datahub-symlink-first)
- [`list`](#datahub-symlink-list)
- [`permissions.`](#datahub-symlink-permissions.)
- [`the`](#datahub-symlink-the)

---

## `plexos-cloud datahub sync`

**Command Path:** `plexos-cloud → datahub → sync`

### Help Output

```
CloudCLI.Commands.Datahub.SyncCommand

Sync's local folders with Datahub folders.

Usage: plexos-cloud datahub sync [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --all              Sync's all current local mappings to/from Datahub.
  --path             Sync's a local path to/from Datahub. Mapping must already
                     exist.
  -v|--verify        Verify the content of the download against the signature.
  --force-download   Force the local version to be overwritten with the server
                     version in case of a conflict.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub undelete`

**Command Path:** `plexos-cloud → datahub → undelete`

### Help Output

```
CloudCLI.Commands.Datahub.UnDeleteCommand

Un-deletes files on Datahub

Usage: plexos-cloud datahub undelete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --pattern          Specify globbing patterns that map to folders or files in
                     datahub for un-deletion (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub unmap-folder`

**Command Path:** `plexos-cloud → datahub → unmap-folder`

### Help Output

```
CloudCLI.Commands.Datahub.Map.UnmapFolderCommand

Unmap a local folder from a remote folder

Usage: plexos-cloud datahub unmap-folder [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --local-folder     Set the local directory folder to unmap
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub upload`

**Command Path:** `plexos-cloud → datahub → upload`

### Help Output

```
CloudCLI.Commands.Datahub.UploadCommand

Upload local files to datahub

Usage: plexos-cloud datahub upload [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --local-folder     Set the local directory path
  --remote-folder    Set the remote datahub path
  --pattern          Set the filter patterns to refine the selection of local
                     files
  --is-versioned     Set the flag to enable versioning
                     Default value is: True.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment browser`

**Command Path:** `plexos-cloud → environment → browser`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'browser'

```

---

## `plexos-cloud environment callback`

**Command Path:** `plexos-cloud → environment → callback`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'callback'

```

---

## `plexos-cloud environment check-install-mapping`

**Command Path:** `plexos-cloud → environment → check-install-mapping`

### Help Output

```
CloudCLI.Commands.Environment.CheckCliMappingCommand

Checks the mapping of the Cloud Toolkit installation path

Usage: plexos-cloud environment check-install-mapping [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --overwrite        Overwrite any file that already exists
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment check-machine-identifiers`

**Command Path:** `plexos-cloud → environment → check-machine-identifiers`

### Help Output

```
CloudCLI.Commands.Environment.CheckMachineIdentifiersCommand

Checks ability to read machine identifying information for licensing purposes

Usage: plexos-cloud environment check-machine-identifiers [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment check-write-registry`

**Command Path:** `plexos-cloud → environment → check-write-registry`

### Help Output

```
CloudCLI.Commands.Environment.CheckCallBackRegistryCommand

Checks ability to write registry values for callback

Usage: plexos-cloud environment check-write-registry [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment diagnostic-information`

**Command Path:** `plexos-cloud → environment → diagnostic-information`

### Help Output

```
CloudCLI.Commands.Environment.GetDiagnosticInformationCommand

Get the diagnostic information

Usage: plexos-cloud environment diagnostic-information [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  --studyId             The ID of the study
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud environment generate-web-link`

**Command Path:** `plexos-cloud → environment → generate-web-link`

### Help Output

```
CloudCLI.Commands.Environment.GenerateWebLinkUrlCommand

Generates a Plexos Cloud Web Url to view in a browser

Usage: plexos-cloud environment generate-web-link [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The Id of the study to view in cloud web
  --modelName        The model name to view in cloud web
  --simulationId     The simulation Id to view in cloud web
  --parameters       Url query parameters (e.g. action=run) to open in cloud web
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment get`

**Command Path:** `plexos-cloud → environment → get`

### Help Output

```
CloudCLI.Commands.Environment.GetUserEnvironmentCommand

Displays the current configured cloud environment

Usage: plexos-cloud environment get [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment information`

**Command Path:** `plexos-cloud → environment → information`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'information'

```

---

## `plexos-cloud environment installation`

**Command Path:** `plexos-cloud → environment → installation`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'installation'

```

---

## `plexos-cloud environment list-users`

**Command Path:** `plexos-cloud → environment → list-users`

### Help Output

```
CloudCLI.Commands.Environment.ListUsersCommand

Get user details for tenant

Usage: plexos-cloud environment list-users [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment logging-path`

**Command Path:** `plexos-cloud → environment → logging-path`

### Help Output

```
CloudCLI.Commands.Environment.ShowLogFilePathCommand

Displays the folder path where log files are saved

Usage: plexos-cloud environment logging-path [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --today            Show the path to today's log file instead of parent
                     directory
                     Default value is: False.
  --open             Opens log file in default log viewer
                     Default value is: False.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment proxy-config`

**Command Path:** `plexos-cloud → environment → proxy-config`

### Help Output

```
CloudCLI.Commands.Environment.EnvironmentProxyConfigCommand

Displays proxy configuration

Usage: plexos-cloud environment proxy-config [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --show-values
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment set`

**Command Path:** `plexos-cloud → environment → set`

### Help Output

```
CloudCLI.Commands.Environment.SetUserEnvironmentCommand

Sets the current configured cloud environment

Usage: plexos-cloud environment set [options] <environment>

Arguments:
  environment        The name of the environment to switch to
                     Allowed values are: Eagles, Aquila, PreProd, Hotfix, NA,
                     EMEA, APAC, AEMO_STG, AEMO_PROD, IND_PROD, NA_BCS, SA_PROD,
                     APAC_BCS, UAE.

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud environment status`

**Command Path:** `plexos-cloud → environment → status`

### Help Output

```
CloudCLI.Commands.Environment.EnvironmentStatusCommand

Displays environment statuses

Usage: plexos-cloud environment status [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud input-data db-to-xml`

**Command Path:** `plexos-cloud → input-data → db-to-xml`

### Help Output

```
CloudCLI.Commands.InputData.ConvertDatabaseToXmlCommand

Convert SQLite database to XML

Usage: plexos-cloud input-data db-to-xml [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -d|--db            DB File Path (required)
  -x|--xml           XML File Path (required)
  -s|--studyId       The ID of the study.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud input-data update`

**Command Path:** `plexos-cloud → input-data → update`

### Help Output

```
CloudCLI.Commands.InputData.UpdateInputDataFromJsonCommand

Update items from json in input data

Usage: plexos-cloud input-data update [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -d|--db            DB File Path (Required)
  -j|--json          Json File Path (Required)
  -s|--studyId       The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud input-data xml-to-db`

**Command Path:** `plexos-cloud → input-data → xml-to-db`

### Help Output

```
CloudCLI.Commands.InputData.ConvertXmlToDatabaseCommand

Convert XML to SQLite database

Usage: plexos-cloud input-data xml-to-db [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -x|--xml           XML File Path (required)
  -d|--db            DB File Path (required)
  -s|--studyId       The ID of the study
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud insights get-machine-recommendation`

**Command Path:** `plexos-cloud → insights → get-machine-recommendation`

### Help Output

```
CloudCLI.Commands.Insights.GetRecommendationForModelCommand

get machine recommendation for group of models

Usage: plexos-cloud insights get-machine-recommendation [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --changesetId      The changeSet ID of the study (required)
  --modelName        Recommendation details for the following model: --modelName
                     "ModelA" --modelName "ModelB" (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud licensing download`

**Command Path:** `plexos-cloud → licensing → download`

### Help Output

```
CloudCLI.Commands.Licensing.DownloadLicenseCommand

Download PLEXOS or Connect license from empty license file

Usage: plexos-cloud licensing download [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -e|--empty         Empty license File Path (Required)
  -o|--output        Destination File Path (Required)
  --overwrite        Overwrite any file that already exists
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud licensing download-aurora`

**Command Path:** `plexos-cloud → licensing → download-aurora`

### Help Output

```
CloudCLI.Commands.Licensing.DownloadAuroraLicenseCommand

Download Aurora license from MachineID and MachineName

Usage: plexos-cloud licensing download-aurora [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -o|--output        Destination File Path (Required)
  -i|--identifier    MachineGuid from target machine registry (Required)
  -n|--name          MachineName from target machine (Required)
  --overwrite        Overwrite any file that already exists
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud licensing refresh`

**Command Path:** `plexos-cloud → licensing → refresh`

### Help Output

```
CloudCLI.Commands.Licensing.RefreshCliLicenseCommand

Refresh CLI license manually

Usage: plexos-cloud licensing refresh [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud log parse`

**Command Path:** `plexos-cloud → log → parse`

### Help Output

```
CloudCLI.Commands.Logs.ParseLogCommand

Parse Simulation Log

Usage: plexos-cloud log parse [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -l|--logfile       Log File Path (required)
  -s|--system        System object name (optional)
  -c|--culture       Culture (optional)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation Subcommands`

**Command Path:** `plexos-cloud → simulation → Subcommands`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'Subcommands'

```

---

## `plexos-cloud simulation build-request-from-previous`

**Command Path:** `plexos-cloud → simulation → build-request-from-previous`

### Help Output

```
CloudCLI.Commands.Simulation.BuildSimulationRequestFromIdCommand

build simulation request based on previously ran simulation

Usage: plexos-cloud simulation build-request-from-previous [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --simulationId        The ID of a simulation ran previously (required)
  --file                File Name (required)
  --changesetId         Override the request's changeset Id with this
  --studyId             Override the request's study Id with this
  --modelName           Override the request's model with this
  --requestedCores      Override the request's desired core count with this
  --requestedMemory     Override the request's desired memory (in Gb) with this
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud simulation cancel`

**Command Path:** `plexos-cloud → simulation → cancel`

### Help Output

```
CloudCLI.Commands.Simulation.CancelSimulationCommand

Cancel Simulation request

Usage: plexos-cloud simulation cancel [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --simulationId     The simulation request Id to be canceled
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation capability`

**Command Path:** `plexos-cloud → simulation → capability`

### Help Output

```
CloudCLI.Commands.Simulation.Capabilities.SimulationPoolCapabilityCommand

Manage capabilities

Usage: plexos-cloud simulation capability [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  list               List capabilities

Run 'capability [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`list`](#simulation-capability-list)

---

## `plexos-cloud simulation different`

**Command Path:** `plexos-cloud → simulation → different`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'different'

```

---

## `plexos-cloud simulation enable`

**Command Path:** `plexos-cloud → simulation → enable`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'enable'

```

---

## `plexos-cloud simulation engine`

**Command Path:** `plexos-cloud → simulation → engine`

### Help Output

```
CloudCLI.Commands.Simulation.Engines.SimulationEngineCommand

Manage engines

Usage: plexos-cloud simulation engine [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  list               List engines
  upload             It uploads, registers, and maps the engine to the tenants
                     specified.

Run 'engine [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`list`](#simulation-engine-list)
- [`specified.`](#simulation-engine-specified.)
- [`upload`](#simulation-engine-upload)

---

## `plexos-cloud simulation enqueue`

**Command Path:** `plexos-cloud → simulation → enqueue`

### Help Output

```
CloudCLI.Commands.Simulation.Enqueue.EnqueueSimulationCommand

Using top-level command with --file option will enable enqueuing simulations from a JSON file. Subcommands (Early Access) manages enqueuing different types of simulations

Usage: plexos-cloud simulation enqueue [command] [options]

Options:
  -f|--format          Output format(json | csv | tsv | yaml | table | none)
                       Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                       YAML.
                       Default value is: JSON.
  -q|--quiet           Turns off verbose messages from app
  -aut|--automation    Turns on developer friendly structured response messages
                       from app
                       Allowed values are: None, PythonSDK.
  --jsonOnly           Show the created JSON body only, or show the request
                       contract if using just enqueue. Does not enqueue a
                       simulation.
  --file               Path to the enqueue simulation request JSON file.
                       (Required)
  --set-context        Set the current context to the new simulation after
                       enqueueing.
  -?|-h|--help         Show help information.

Commands:
  chronological-split  (Early Access) Enqueues a chronological split simulation.
                       Command is in early access so specific arguments and
                       responses are subject to change.
  custom-plexos        (Early Access) Enqueues a simulation in Plexos that
                       allows for custom arguments. Command is in early access
                       so specific arguments and responses are subject to
                       change.
  gurobi               (Early Access) Enqueues a Gurobi tuning job. Command is
                       in early access so specific arguments and responses are
                       subject to change.
  monte-carlo          (Early Access) Enqueues a Monte Carlo (V2) simulation.
                       Command is in early access so specific arguments and
                       responses are subject to change.
  standard             (Early Access) Enqueues a standard simulation in Plexos
                       using arguments. Can also be used as a starting point to
                       build requests with the default type. Command is in early
                       access so specific arguments and responses are subject to
                       change.
  stochastic           (Early Access) Enqueues a stochastic (Monte Carlo V1)
                       simulation. Command is in early access so specific
                       arguments and responses are subject to change.

Run 'enqueue [command] -?|-h|--help' for more information about a command.
All subcommands are in early access and subject to change. The sub commands are argument based, and only requires a few items such as Study ID, model names, etc. Each command will have specific options that apply to that simulation type, and are optional unless otherwise specified.


```

### Available Subcommands

- [`Command`](#simulation-enqueue-command)
- [`Command`](#simulation-enqueue-command)
- [`access`](#simulation-enqueue-access)
- [`allows`](#simulation-enqueue-allows)
- [`arguments`](#simulation-enqueue-arguments)
- [`build`](#simulation-enqueue-build)
- [`change.`](#simulation-enqueue-change.)
- [`change.`](#simulation-enqueue-change.)
- [`chronological-split`](#simulation-enqueue-chronological-split)
- [`custom-plexos`](#simulation-enqueue-custom-plexos)
- [`gurobi`](#simulation-enqueue-gurobi)
- [`in`](#simulation-enqueue-in)
- [`monte-carlo`](#simulation-enqueue-monte-carlo)
- [`responses`](#simulation-enqueue-responses)
- [`responses`](#simulation-enqueue-responses)
- [`simulation.`](#simulation-enqueue-simulation.)
- [`so`](#simulation-enqueue-so)
- [`standard`](#simulation-enqueue-standard)
- [`stochastic`](#simulation-enqueue-stochastic)
- [`subject`](#simulation-enqueue-subject)
- [`using`](#simulation-enqueue-using)

---

## `plexos-cloud simulation in`

**Command Path:** `plexos-cloud → simulation → in`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'in'

```

---

## `plexos-cloud simulation list`

**Command Path:** `plexos-cloud → simulation → list`

### Help Output

```
CloudCLI.Commands.Simulation.ListSimulationsCommand

List simulations

Usage: plexos-cloud simulation list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --simulationId     Filter by the simulation ID
  --studyId          Filter by the study ID
  --executionId      Filter by the executionId ID
  --changesetId      Filter by the Changeset ID
  --orderBy          Set the property to order results by
                     Allowed values are: Id, ExecutionId, StudyId, ChangeSetId,
                     Source, RequestedCpuCores, MinimumMemoryInGb, CreatedAt,
                     LastUpdatedAt, Status, RetryCount, ParallelizationOptions.
  --descending       Order the property descending
  --top              Select the top N results
  --skip             Skip the next N results
  --raw              A raw string passed directly to odata endpoint, encased in
                     double quotes. Cannot be used with other odata options
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation monitor`

**Command Path:** `plexos-cloud → simulation → monitor`

### Help Output

```
CloudCLI.Commands.Simulation.MonitorSimulationProgressCommand

Monitor Simulations while they are running, i.e. in progress state

Usage: plexos-cloud simulation monitor [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --simulationId     The simulation to monitor
  --output           (StepData) Parsed Step Data, (Raw) Raw Log from Engine,
                     (Utilization) Resource Utilization data only.
                     Allowed values are: StepData, Raw, Utilization, Progress.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation progress`

**Command Path:** `plexos-cloud → simulation → progress`

### Help Output

```
CloudCLI.Commands.Simulation.CheckSimmulationProgressCommand

Check Simulation progress

Usage: plexos-cloud simulation progress [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --simulationId     The simulation request Id to Check Current Proggress
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation run-group`

**Command Path:** `plexos-cloud → simulation → run-group`

### Help Output

```
CloudCLI.Commands.Simulation.RunSimulationGroupCommand

Runs the simulation group.

Usage: plexos-cloud simulation run-group [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --groupId          The simulation group id to be triggered (Required)
  --studyId          The study identifier. (Required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation simulation`

**Command Path:** `plexos-cloud → simulation → simulation`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'simulation'

```

---

## `plexos-cloud solution archive`

**Command Path:** `plexos-cloud → solution → archive`

### Help Output

```
CloudCLI.Commands.Solution.ArchiveSolutionCommand

This command will archive all solutions associated with the execution.

Usage: plexos-cloud solution archive [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --executionId      The ID of the execution (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution bi`

**Command Path:** `plexos-cloud → solution → bi`

### Help Output

```
CloudCLI.Commands.Solution.Bi.BiCommand

Manage Bi

Usage: plexos-cloud solution bi [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  delete             Unpublishes the solution from BI Analytics
  list               Fetches published solutions from BI Analytics, optionally
                     filtered by study ID.
  publish            Publishes the solution to BI Analytics
  status             Fetches the status of the solution added in BI Analytics
                     based on SolutionId

Run 'bi [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`based`](#solution-bi-based)
- [`delete`](#solution-bi-delete)
- [`filtered`](#solution-bi-filtered)
- [`list`](#solution-bi-list)
- [`publish`](#solution-bi-publish)
- [`status`](#solution-bi-status)

---

## `plexos-cloud solution convert`

**Command Path:** `plexos-cloud → solution → convert`

### Help Output

```
CloudCLI.Commands.Solution.Convert.ConvertSolutionDataCommand

Commands dealing with converting solution databases

Usage: plexos-cloud solution convert [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  condense-file      Converts the given LP/MIP into a smaller lp file with
                     Objectives, constraints, bounds related to a particular
                     period
  hybrid-to-parquet  Converts the PLEXOS Cloud hybrid (sqlite + parquet)
                     database format to the full parquet database structure
  zip-to-hybrid      Converts the PLEXOS zip output database to a hybrid format
                     of sqlite with parquet data
  zip-to-parquet     Converts the PLEXOS zip output database to a parquet format

Run 'convert [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`Objectives,`](#solution-convert-objectives,)
- [`condense-file`](#solution-convert-condense-file)
- [`database`](#solution-convert-database)
- [`hybrid-to-parquet`](#solution-convert-hybrid-to-parquet)
- [`of`](#solution-convert-of)
- [`period`](#solution-convert-period)
- [`zip-to-hybrid`](#solution-convert-zip-to-hybrid)
- [`zip-to-parquet`](#solution-convert-zip-to-parquet)

---

## `plexos-cloud solution delete`

**Command Path:** `plexos-cloud → solution → delete`

### Help Output

```
CloudCLI.Commands.Solution.DeleteSolutionCommand

This command will delete all solutions associated with the given execution.(**this is permanent and cannot be undone.)

Usage: plexos-cloud solution delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --executionId      The ID of the solution (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution files`

**Command Path:** `plexos-cloud → solution → files`

### Help Output

```
CloudCLI.Commands.Solution.Files.SolutionFilesCommand

Commands dealing with solution files

Usage: plexos-cloud solution files [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  download           Download data related to a solution
  list               List files for a solution
  list-types         List available file types for a solution

Run 'files [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`download`](#solution-files-download)
- [`list`](#solution-files-list)
- [`list-types`](#solution-files-list-types)

---

## `plexos-cloud solution latest-id`

**Command Path:** `plexos-cloud → solution → latest-id`

### Help Output

```
CloudCLI.Commands.Solution.GetSolutionIdCommand

Gets most recent solution id created for a study & model

Usage: plexos-cloud solution latest-id [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --model            Model Name (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution list`

**Command Path:** `plexos-cloud → solution → list`

### Help Output

```
CloudCLI.Commands.Solution.ListSolutionsCommand

List all solutions

Usage: plexos-cloud solution list [options]

Options:
  -f|--format                 Output format(json | csv | tsv | yaml | table |
                              none)
                              Allowed values are: JSON, JSONL, CSV, None, Table,
                              TSV, YAML.
                              Default value is: JSON.
  -q|--quiet                  Turns off verbose messages from app
  -aut|--automation           Turns on developer friendly structured response
                              messages from app
                              Allowed values are: None, PythonSDK.
  --solutionId                Filter by the Solution Id
  --studyId                   Filter by the Study Id
  --simulationId              Filter by Simulation Id
  --executionId               Filter by Execution Id
  --stitchedFromSimulationId  Only for stitched solution types
                              (StitchedParquet/StitchedHybrid). Will filter for
                              solutions stitched with a source using this
                              simulation Id
  --stitchedFromExecutionId   Only for stitched solution types
                              (StitchedParquet/StitchedHybrid). Will filter for
                              solutions stitched with a source using this
                              execution Id
  --type                      Filter by the solution type
  --status                    Filter by the status type
                              Allowed values are: New, Processing, Complete,
                              Cancelled, Error, Queued, PendingCancel, Deleted.
  --orderBy                   Set the property to order results by
                              Allowed values are: SolutionId, StudyId,
                              ExecutionId, SimulationId, Type, Status,
                              LastUpdatedDate, CreatedDate, ModelName,
                              TypeVersion.
  --descending                Order the property descending
  --top                       Select the top N results
  --skip                      Skip the next N results
  --raw                       A raw string passed directly to odata endpoint,
                              encased in double quotes. Cannot be used with
                              other odata options
  -?|-h|--help                Show help information.


```

---

## `plexos-cloud solution list-reports`

**Command Path:** `plexos-cloud → solution → list-reports`

### Help Output

```
CloudCLI.Commands.Solution.ListSolutionReportsCommand

List Solution Reports

Usage: plexos-cloud solution list-reports [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution model`

**Command Path:** `plexos-cloud → solution → model`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'model'

```

---

## `plexos-cloud solution query`

**Command Path:** `plexos-cloud → solution → query`

### Help Output

```
CloudCLI.Commands.Solution.Query.QuerySolutionDataCommand

Commands dealing with query solution data

Usage: plexos-cloud solution query [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  configure-views    Configures DuckDb views to simplify parquet querying by
                     model

Run 'query [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`configure-views`](#solution-query-configure-views)
- [`model`](#solution-query-model)

---

## `plexos-cloud solution solution-report-upload`

**Command Path:** `plexos-cloud → solution → solution-report-upload`

### Help Output

```
CloudCLI.Commands.Solution.SolutionReportUploadCommand

Uploads a solution report

Usage: plexos-cloud solution solution-report-upload [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --file             Path to the configuration file
  --reportName       name of the report
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution solution-reports`

**Command Path:** `plexos-cloud → solution → solution-reports`

### Help Output

```
CloudCLI.Commands.Solution.SolutionReportsCommand

gets solution report data

Usage: plexos-cloud solution solution-reports [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --solutionId          solution ID (required)
  --reportId            ID of the report (required)
  --file                file name
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud solution solution-stitching`

**Command Path:** `plexos-cloud → solution → solution-stitching`

### Help Output

```
CloudCLI.Commands.Solution.SolutionStitchingCommand

stitch multiple solutions together to get new solution

Usage: plexos-cloud solution solution-stitching [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --executionId      Id for execution (Required)
  --cores            Total number of cores (Required)
  --memory           Total memory usage(Required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution the`

**Command Path:** `plexos-cloud → solution → the`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'the'

```

---

## `plexos-cloud solution unarchive`

**Command Path:** `plexos-cloud → solution → unarchive`

### Help Output

```
CloudCLI.Commands.Solution.UnarchiveSolutionCommand

This command will unarchive all solutions associated with the given execution.

Usage: plexos-cloud solution unarchive [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --executionId      The ID of the execution (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution undone.)`

**Command Path:** `plexos-cloud → solution → undone.)`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'undone.)'

```

---

## `plexos-cloud solution view`

**Command Path:** `plexos-cloud → solution → view`

### Help Output

```
CloudCLI.Commands.Solution.View.ViewCommand

Manage views

Usage: plexos-cloud solution view [command] [options]

Options:
  -f|--format                      Output format(json | csv | tsv | yaml | table
                                   | none)
                                   Allowed values are: JSON, JSONL, CSV, None,
                                   Table, TSV, YAML.
                                   Default value is: JSON.
  -q|--quiet                       Turns off verbose messages from app
  -aut|--automation                Turns on developer friendly structured
                                   response messages from app
                                   Allowed values are: None, PythonSDK.
  -?|-h|--help                     Show help information.

Commands:
  get-downloadable-report-details  Get view report details along with commands
                                   for all the reports in View for downloading
                                   report data
  get-report-data                  Get solution report data
  list                             List of assigned views
  publish                          Publish a view

Run 'view [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`for`](#solution-view-for)
- [`get-downloadable-report-details`](#solution-view-get-downloadable-report-details)
- [`get-report-data`](#solution-view-get-report-data)
- [`list`](#solution-view-list)
- [`publish`](#solution-view-publish)
- [`report`](#solution-view-report)

---

## `plexos-cloud solution with`

**Command Path:** `plexos-cloud → solution → with`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'with'

```

---

## `plexos-cloud study archive`

**Command Path:** `plexos-cloud → study → archive`

### Help Output

```
CloudCLI.Commands.Study.ArchiveStudyCommand

Archive the given Study

Usage: plexos-cloud study archive [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --deleteSolutions  Delete all solutions in this Study
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset`

**Command Path:** `plexos-cloud → study → changeset`

### Help Output

```
CloudCLI.Commands.Study.Changesets.StudyChangesetCommand

Commands dealing with a study's changeset

Usage: plexos-cloud study changeset [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  download           Downloads XML and timeseries (if applicable) files for a
                     study's changeset. Changes to these files will not be
                     tracked by the study by default.
  get-latest         Gets Latest Changeset ID for Study.
  get-latest-local   Gets Latest Local Changeset ID for Study.
  get-status         Fetches the changeset status of the current study, if there
                     are incoming/outgoing changesets or the study is in sync
  get-urls           List the download URLS for this changeset. Only used for
                     building a simulation enqueue request for this changeset,
                     using the URLS still requires API authentication
  list               List the changesets for a study
  list-local         List the local changesets for a study
  pull               Pull the latest changes for a study
  push               Push the latest changes for a study

Run 'changeset [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`are`](#study-changeset-are)
- [`building`](#study-changeset-building)
- [`download`](#study-changeset-download)
- [`get-latest`](#study-changeset-get-latest)
- [`get-latest-local`](#study-changeset-get-latest-local)
- [`get-status`](#study-changeset-get-status)
- [`get-urls`](#study-changeset-get-urls)
- [`list`](#study-changeset-list)
- [`list-local`](#study-changeset-list-local)
- [`pull`](#study-changeset-pull)
- [`push`](#study-changeset-push)
- [`study's`](#study-changeset-study's)
- [`tracked`](#study-changeset-tracked)
- [`using`](#study-changeset-using)

---

## `plexos-cloud study clone`

**Command Path:** `plexos-cloud → study → clone`

### Help Output

```
CloudCLI.Commands.Study.CloneStudyCommand

Downloads and initializes a tracked study from the cloud

Usage: plexos-cloud study clone [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  --studyId             The ID of the study (required)
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud study create`

**Command Path:** `plexos-cloud → study → create`

### Help Output

```
CloudCLI.Commands.Study.CreateStudyCommand

Creates a study from input project file

Usage: plexos-cloud study create [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --name             A name for the study (required)
  --description      A description for the study (required)
  --database         Path to the input project file (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study data`

**Command Path:** `plexos-cloud → study → data`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'data'

```

---

## `plexos-cloud study delete`

**Command Path:** `plexos-cloud → study → delete`

### Help Output

```
CloudCLI.Commands.Study.DeleteStudyCommand

Delete the given study from PLEXOS Cloud. (**this is permanent and cannot be undone.)

Usage: plexos-cloud study delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study delete-local`

**Command Path:** `plexos-cloud → study → delete-local`

### Help Output

```
CloudCLI.Commands.Study.DeleteLocalStudyCommand

Deletes local study files

Usage: plexos-cloud study delete-local [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --full-delete      Deletes all local study data, including XML and Timeseries
                     data
  --database         Path to study's xml file. May be required for delete
                     operations in case study is corrupted
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study find`

**Command Path:** `plexos-cloud → study → find`

### Help Output

```
CloudCLI.Commands.Study.FindStudyCommand

Find the Study by name

Usage: plexos-cloud study find [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyName        Filter by the Study Name
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study grant-user-access`

**Command Path:** `plexos-cloud → study → grant-user-access`

### Help Output

```
CloudCLI.Commands.Study.GrantUserAccessCommand

Grants user access to a study

Usage: plexos-cloud study grant-user-access [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --userEmail        The userEmail to be given access (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study list`

**Command Path:** `plexos-cloud → study → list`

### Help Output

```
CloudCLI.Commands.Study.ListStudiesCommand

List studies

Usage: plexos-cloud study list [options]

Options:
  -f|--format             Output format(json | csv | tsv | yaml | table | none)
                          Allowed values are: JSON, JSONL, CSV, None, Table,
                          TSV, YAML.
                          Default value is: JSON.
  -q|--quiet              Turns off verbose messages from app
  -aut|--automation       Turns on developer friendly structured response
                          messages from app
                          Allowed values are: None, PythonSDK.
  --type                  Filter by the study type
                          Allowed values are: Plexos, Aurora.
  --orderBy               Set the property to order results by
                          Allowed values are: Id, Name, Description, Status,
                          LastUpdateMessage, CreatedDate, LastUpdatedAtUtc,
                          StudyType, isAccessibleToRequestingUser.
  --descending            Order the property descending
  --top                   Select the top N results
  --skip                  Skip the next N results
  --raw                   A raw string passed directly to odata endpoint,
                          encased in double quotes. Cannot be used with other
                          odata options
  --studyId               Filter by the Study Id
  --filterForCurrentUser  filter by current user
  -?|-h|--help            Show help information.


```

---

## `plexos-cloud study list-local`

**Command Path:** `plexos-cloud → study → list-local`

### Help Output

```
CloudCLI.Commands.Study.ListLocalStudiesCommand

List local studies that are tracked on the cloud

Usage: plexos-cloud study list-local [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study list-local-studyIDs`

**Command Path:** `plexos-cloud → study → list-local-studyIDs`

### Help Output

```
CloudCLI.Commands.Study.ListStudyIdsForFolderCommand

Lists PLEXOS Cloud study IDs currently attached to a local study directory

Usage: plexos-cloud study list-local-studyIDs [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyDir         Path to the PLEXOS Cloud study directory. Should be
                     directory where study XML database exists.(required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study local`

**Command Path:** `plexos-cloud → study → local`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'local'

```

---

## `plexos-cloud study permanent`

**Command Path:** `plexos-cloud → study → permanent`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'permanent'

```

---

## `plexos-cloud study repair-local`

**Command Path:** `plexos-cloud → study → repair-local`

### Help Output

```
CloudCLI.Commands.Study.StudyRepairCommand

Attempts to repair the cloud sync of a local study when data has been corrupted or study gets moved

Usage: plexos-cloud study repair-local [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --database         Path to study's xml file. May be required for some repair
                     operations
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study reset`

**Command Path:** `plexos-cloud → study → reset`

### Help Output

```
CloudCLI.Commands.Study.ResetStudyCommand

Reset study on local to latest version on cloud

Usage: plexos-cloud study reset [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study settings`

**Command Path:** `plexos-cloud → study → settings`

### Help Output

```
CloudCLI.Commands.Study.Settings.SettingsCommand

Manage studies settings

Usage: plexos-cloud study settings [command] [options]

Options:
  -f|--format         Output format(json | csv | tsv | yaml | table | none)
                      Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                      YAML.
                      Default value is: JSON.
  -q|--quiet          Turns off verbose messages from app
  -aut|--automation   Turns on developer friendly structured response messages
                      from app
                      Allowed values are: None, PythonSDK.
  -?|-h|--help        Show help information.

Commands:
  add-configurations  Add configurations to the existing study settings
  create              create study settings based on settings type.
  delete              Delete the study settings
  list                List the study settings available for the given study

Run 'settings [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`add-configurations`](#study-settings-add-configurations)
- [`create`](#study-settings-create)
- [`delete`](#study-settings-delete)
- [`list`](#study-settings-list)

---

## `plexos-cloud study stats`

**Command Path:** `plexos-cloud → study → stats`

### Help Output

```
CloudCLI.Commands.Study.StudyStats.StudyStatsCommand

Commands dealing with a study's statistical information

Usage: plexos-cloud study stats [command] [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.

Commands:
  geocoded-objects   Number of geocoded Objects

Run 'stats [command] -?|-h|--help' for more information about a command.


```

### Available Subcommands

- [`geocoded-objects`](#study-stats-geocoded-objects)

---

## `plexos-cloud study unarchive`

**Command Path:** `plexos-cloud → study → unarchive`

### Help Output

```
CloudCLI.Commands.Study.UnarchiveStudyCommand

Unarchive the given Study

Usage: plexos-cloud study unarchive [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study validate`

**Command Path:** `plexos-cloud → study → validate`

### Help Output

```
CloudCLI.Commands.Study.ValidateStudyDataCommand

Validate data for study creation

Usage: plexos-cloud study validate [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --database         Path to the PLEXOS input xml database file (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud tool install`

**Command Path:** `plexos-cloud → tool → install`

### Help Output

```
CloudCLI.Commands.Tool.InstallToolCommand

Install an available tool

Usage: plexos-cloud tool install [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --name             Tool Name
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud tool list`

**Command Path:** `plexos-cloud → tool → list`

### Help Output

```
CloudCLI.Commands.Tool.ListToolsCommand

List available tools.

Usage: plexos-cloud tool list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud tool run`

**Command Path:** `plexos-cloud → tool → run`

### Help Output

```
CloudCLI.Commands.Tool.RunToolCommand

Run an installed tool

Usage: plexos-cloud tool run [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --name             Name of the tool
  --args             Arguments to pass to the tool
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud tool vscode`

**Command Path:** `plexos-cloud → tool → vscode`

### Help Output

```
CloudCLI.Commands.Tool.VsCode.VsCodeCommand

VSCode management

Usage: plexos-cloud tool vscode [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --args             Arguments to pass to 'code'
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud upgrade check`

**Command Path:** `plexos-cloud → upgrade → check`

### Help Output

```
CloudCLI.Commands.Upgrade.CheckUpgradeCommand

Check for newer version

Usage: plexos-cloud upgrade check [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud upgrade install`

**Command Path:** `plexos-cloud → upgrade → install`

### Help Output

```
CloudCLI.Commands.Upgrade.InstallUpgradeCommand

Install upgrade if newer exists

Usage: plexos-cloud upgrade install [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud users create`

**Command Path:** `plexos-cloud → users → create`

### Help Output

```
CloudCLI.Commands.Identity.CreateUserCommand

Beta: Create users in bulk from a csv file

Usage: plexos-cloud users create [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --file-path        Set the file path (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud users downloadtemplate`

**Command Path:** `plexos-cloud → users → downloadtemplate`

### Help Output

```
CloudCLI.Commands.Identity.DownloadCreateUserCSVTemplateCommand

Beta: Download csv template for creating users

Usage: plexos-cloud users downloadtemplate [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --out-file-path    Set the output file path (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub permission Do`

**Command Path:** `plexos-cloud → datahub → permission → Do`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'Do'

```

---

## `plexos-cloud datahub permission add-update`

**Command Path:** `plexos-cloud → datahub → permission → add-update`

### Help Output

```
CloudCLI.Commands.Datahub.Permission.AddOrUpdatePermissionCommand

Add or update ACL permissions on datahub.

Usage: plexos-cloud datahub permission add-update [options]

Options:
  -f|--format                   Output format(json | csv | tsv | yaml | table |
                                none)
                                Allowed values are: JSON, JSONL, CSV, None,
                                Table, TSV, YAML.
                                Default value is: JSON.
  -q|--quiet                    Turns off verbose messages from app
  -aut|--automation             Turns on developer friendly structured response
                                messages from app
                                Allowed values are: None, PythonSDK.
  -p|--remote-path              Set the remote directory or remote file on which
                                the permission will apply to.
  -h|--inheritParentPermission  Set whether or not the parent folder permissions
                                will apply to this permission in addition to. Do
                                not use this flag if you are not sure.
  -t|--permissionType           Set if the permission is for a User or a Role
                                Allowed values are: Role, User.
  --id                          Set the Id of the user or the role depending on
                                which type was selected
  -r|--read                     Set the read permission
  -w|--write                    Set the write permission
  -?|-h|--help                  Show help information.


```

---

## `plexos-cloud datahub permission delete`

**Command Path:** `plexos-cloud → datahub → permission → delete`

### Help Output

```
CloudCLI.Commands.Datahub.Permission.DeletePermissionCommand

Deletes a single permission on an ACL rule

Usage: plexos-cloud datahub permission delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -p|--remote-path   Set the remote directory or remote file on which the
                     permission will apply to.
  -r|--role          Set the roles to delete the permission from
  -u|--user-id       Set the user ids to delete the permission from
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub permission delete-rule`

**Command Path:** `plexos-cloud → datahub → permission → delete-rule`

### Help Output

```
CloudCLI.Commands.Datahub.Permission.DeletePermissionRuleCommand

Deletes the entire ACL rule

Usage: plexos-cloud datahub permission delete-rule [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -p|--remote-path   Set the remote directory or remote file for which the rule
                     should be removed
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub permission list`

**Command Path:** `plexos-cloud → datahub → permission → list`

### Help Output

```
CloudCLI.Commands.Datahub.Permission.ListPermissionsCommand

List all permissions

Usage: plexos-cloud datahub permission list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub permission update-inheritParentPermission`

**Command Path:** `plexos-cloud → datahub → permission → update-inheritParentPermission`

### Help Output

```
CloudCLI.Commands.Datahub.Permission.UpdateInheritPermissionCommand

Flip the Inherit Parent permission for a rule. Do not use this command if you are not sure

Usage: plexos-cloud datahub permission update-inheritParentPermission [options]

Options:
  -f|--format                   Output format(json | csv | tsv | yaml | table |
                                none)
                                Allowed values are: JSON, JSONL, CSV, None,
                                Table, TSV, YAML.
                                Default value is: JSON.
  -q|--quiet                    Turns off verbose messages from app
  -aut|--automation             Turns on developer friendly structured response
                                messages from app
                                Allowed values are: None, PythonSDK.
  -p|--remote-path              Set the remote directory or remote file on which
                                the setting will apply to.
  -h|--inheritParentPermission  Set whether or not the parent folder permissions
                                will apply to this permission in addition to.
  -?|-h|--help                  Show help information.


```

---

## `plexos-cloud datahub share be`

**Command Path:** `plexos-cloud → datahub → share → be`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'be'

```

---

## `plexos-cloud datahub share create`

**Command Path:** `plexos-cloud → datahub → share → create`

### Help Output

```
CloudCLI.Commands.Datahub.Share.CreateShareCommand

Creates a share, which designates a Datahub folder that can be shared and linked to by other tenants.

Usage: plexos-cloud datahub share create [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --name             The name for the share to be created (required)
  --path             The intended remote path to establish the share at, which
                     can be a folder or a file (required)
  --permission       A permission rule to be applied to the share. Formatted as
                     a CSV line: <scope: any>,<tenant ID: guid>,<user ID: guid>
  --permission-file  Path to a CSV file containing permission rules to be
                     applied to the share. Cannot be used with --permission
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub share delete`

**Command Path:** `plexos-cloud → datahub → share → delete`

### Help Output

```
CloudCLI.Commands.Datahub.Share.DeleteShareCommand

Deletes a share.

Usage: plexos-cloud datahub share delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -i|--id            The ID of the share to delete.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub share list`

**Command Path:** `plexos-cloud → datahub → share → list`

### Help Output

```
CloudCLI.Commands.Datahub.Share.ListSharesCommand

Lists all shares in Datahub.

Usage: plexos-cloud datahub share list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub symlink another`

**Command Path:** `plexos-cloud → datahub → symlink → another`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'another'

```

---

## `plexos-cloud datahub symlink create-cross-tenant`

**Command Path:** `plexos-cloud → datahub → symlink → create-cross-tenant`

### Help Output

```
CloudCLI.Commands.Datahub.Symlink.CreateSymlinkCommand

Creates a symlink to a file or folder that is present in another tenant in the same Environment. This requires to first create a Share on the target tenant and set permissions.

Usage: plexos-cloud datahub symlink create-cross-tenant [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --name             The name for the symlink to be created (required)
  -t|--tenantId      The ID of the tenant the symlink is targeting (required)
  --targetPath       Path for the symlink to link to on the other tenant
                     (required)
  --symlinkPath      Path for the symlink to be placed at (required)
  --symlinkType      The type of symlink (File or Directory) (required)
                     Allowed values are: File, Directory.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub symlink create-local`

**Command Path:** `plexos-cloud → datahub → symlink → create-local`

### Help Output

```
CloudCLI.Commands.Datahub.Symlink.CreateLocalSymlinkCommand

Creates a symlink to a file or folder that is present in the same Tenant.

Usage: plexos-cloud datahub symlink create-local [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --name             The name for the symlink to be created (required)
  --targetPath       Path for the symlink to link to on the current tenant
                     (required)
  --symlinkPath      Path for the symlink to be placed at (required)
  --symlinkType      The type of symlink (File or Directory) (required)
                     Allowed values are: File, Directory.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub symlink delete`

**Command Path:** `plexos-cloud → datahub → symlink → delete`

### Help Output

```
CloudCLI.Commands.Datahub.Symlink.DeleteSymlinkCommand

Deletes a symlink.

Usage: plexos-cloud datahub symlink delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -p|--path          The path of the symlink to delete.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub symlink first`

**Command Path:** `plexos-cloud → datahub → symlink → first`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'first'

```

---

## `plexos-cloud datahub symlink list`

**Command Path:** `plexos-cloud → datahub → symlink → list`

### Help Output

```
CloudCLI.Commands.Datahub.Symlink.ListSymlinksCommand

Lists all symlinks in Datahub.

Usage: plexos-cloud datahub symlink list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud datahub symlink permissions.`

**Command Path:** `plexos-cloud → datahub → symlink → permissions.`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'permissions.'

```

---

## `plexos-cloud datahub symlink the`

**Command Path:** `plexos-cloud → datahub → symlink → the`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'the'

```

---

## `plexos-cloud simulation capability list`

**Command Path:** `plexos-cloud → simulation → capability → list`

### Help Output

```
CloudCLI.Commands.Simulation.Capabilities.ListSimulationPoolCapabilityCommand

List capabilities

Usage: plexos-cloud simulation capability list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation engine list`

**Command Path:** `plexos-cloud → simulation → engine → list`

### Help Output

```
CloudCLI.Commands.Simulation.Engines.ListSimulationEngineCommand

List engines

Usage: plexos-cloud simulation engine list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -t|--type          Filters Engines by Optimization engine type
                     Allowed values are: Plexos, Aurora, GurobiTuner.
                     Default value is: Plexos.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation engine specified.`

**Command Path:** `plexos-cloud → simulation → engine → specified.`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'specified.'

```

---

## `plexos-cloud simulation engine upload`

**Command Path:** `plexos-cloud → simulation → engine → upload`

### Help Output

```
CloudCLI.Commands.Simulation.Engines.UploadEngineCommand

It uploads, registers, and maps the engine to the tenants specified.

Usage: plexos-cloud simulation engine upload [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --showExample      Show an example configuration file template
  --file             Path to the configuration file
  -p|--enginePath    Engine file path to be uploaded, Supported format - zip.
                     (Required)
  --tenantId         List of tenant IDs for mapping format :tenantId1,tenantId2
                     (Required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud simulation enqueue Command`

**Command Path:** `plexos-cloud → simulation → enqueue → Command`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'Command'

```

---

## `plexos-cloud simulation enqueue access`

**Command Path:** `plexos-cloud → simulation → enqueue → access`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'access'

```

---

## `plexos-cloud simulation enqueue allows`

**Command Path:** `plexos-cloud → simulation → enqueue → allows`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'allows'

```

---

## `plexos-cloud simulation enqueue arguments`

**Command Path:** `plexos-cloud → simulation → enqueue → arguments`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'arguments'

```

---

## `plexos-cloud simulation enqueue build`

**Command Path:** `plexos-cloud → simulation → enqueue → build`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'build'

```

---

## `plexos-cloud simulation enqueue change.`

**Command Path:** `plexos-cloud → simulation → enqueue → change.`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'change.'

```

---

## `plexos-cloud simulation enqueue chronological-split`

**Command Path:** `plexos-cloud → simulation → enqueue → chronological-split`

### Help Output

```
CloudCLI.Commands.Simulation.Enqueue.EnqueueSplitSimulationCommand

(Early Access) Enqueues a chronological split simulation. Command is in early access so specific arguments and responses are subject to change.

Usage: plexos-cloud simulation enqueue chronological-split [options]

Options:
  -f|--format               Output format(json | csv | tsv | yaml | table |
                            none)
                            Allowed values are: JSON, JSONL, CSV, None, Table,
                            TSV, YAML.
                            Default value is: JSON.
  -q|--quiet                Turns off verbose messages from app
  -aut|--automation         Turns on developer friendly structured response
                            messages from app
                            Allowed values are: None, PythonSDK.
  --jsonOnly                Show the created JSON body only, or show the request
                            contract if using just enqueue. Does not enqueue a
                            simulation.
  --studyId                 Study ID (required)
  --models                  Models (required)
  --engineId                Engine ID (required)
  --changesetId             Changeset ID (optional) (latest changeset from study
                            is default)
  --cpuCores                CPU Cores (required)
  --memoryInGb              Memory in GB (required)
  --locale                  Locale (optional) (1033 - en-US - default)
  --parquetVersion          Parquet Version (deprecated) (2 default)
  --simulationDataTypes     Simulation Data Types (optional) (Default is
                            ChangesetDatabase, TimeseriesZipped)
                            Allowed values are: ChangesetDatabase,
                            TimeseriesDatabase, ZippedXmlInput, ZippedExtras,
                            TimeseriesZipped, AncillaryZippedInput, LocalXml,
                            ZippedAuroraInput, ZippedManifests.
  --simulationRunType       Simulation Run Type (optional) (Default is
                            SingleRun)
                            Allowed values are: ModelDistributionRun,
                            MultipleVmSelectionRun, SingleRun.
  --enableSnapshots         Enable PLEXOS Snapshots (optional)
  --snapshotInterval        Snapshot Interval in minutes (--enableSnapshots must
                            be used)
  --exportContractPath      If specified, this will export the enqueue request
                            into a JSON file (enqueueRequest.json) at the
                            specified path (optional)
  --set-context             Set the current context to the new simulation after
                            enqueueing.
  --split-divisions         Number of divisions to split the simulation into.
                            (required)
  --split-step-type         Chronological type to split as (required)
                            Allowed values are: Minute, Hour, Day, Week, Month,
                            Second.
  --run-as-single-instance  Run the simulation on a single instance. (optional)
                            (False default)
  --child-cpu-cores         Specifies the number of CPU cores that a split child
                            will use. (required)
  --child-memory-in-GB      Specifies how much memory each child instance should
                            have. (required)
  -?|-h|--help              Show help information.


```

---

## `plexos-cloud simulation enqueue custom-plexos`

**Command Path:** `plexos-cloud → simulation → enqueue → custom-plexos`

### Help Output

```
CloudCLI.Commands.Simulation.Enqueue.CustomPlexosSimulationCommand

(Early Access) Enqueues a simulation in Plexos that allows for custom arguments. Command is in early access so specific arguments and responses are subject to change.

Usage: plexos-cloud simulation enqueue custom-plexos [options]

Options:
  -f|--format            Output format(json | csv | tsv | yaml | table | none)
                         Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                         YAML.
                         Default value is: JSON.
  -q|--quiet             Turns off verbose messages from app
  -aut|--automation      Turns on developer friendly structured response
                         messages from app
                         Allowed values are: None, PythonSDK.
  --jsonOnly             Show the created JSON body only, or show the request
                         contract if using just enqueue. Does not enqueue a
                         simulation.
  --studyId              Study ID (required)
  --models               Models (required)
  --engineId             Engine ID (required)
  --changesetId          Changeset ID (optional) (latest changeset from study is
                         default)
  --cpuCores             CPU Cores (required)
  --memoryInGb           Memory in GB (required)
  --locale               Locale (optional) (1033 - en-US - default)
  --parquetVersion       Parquet Version (deprecated) (2 default)
  --simulationDataTypes  Simulation Data Types (optional) (Default is
                         ChangesetDatabase, TimeseriesZipped)
                         Allowed values are: ChangesetDatabase,
                         TimeseriesDatabase, ZippedXmlInput, ZippedExtras,
                         TimeseriesZipped, AncillaryZippedInput, LocalXml,
                         ZippedAuroraInput, ZippedManifests.
  --simulationRunType    Simulation Run Type (optional) (Default is SingleRun)
                         Allowed values are: ModelDistributionRun,
                         MultipleVmSelectionRun, SingleRun.
  --enableSnapshots      Enable PLEXOS Snapshots (optional)
  --snapshotInterval     Snapshot Interval in minutes (--enableSnapshots must be
                         used)
  --exportContractPath   If specified, this will export the enqueue request into
                         a JSON file (enqueueRequest.json) at the specified path
                         (optional)
  --set-context          Set the current context to the new simulation after
                         enqueueing.
  --custom-arguments     Custom arguments to pass to Plexos. (optional)
  -?|-h|--help           Show help information.
This applies only to the Plexos engine - attempts to use Aurora will fail.

```

---

## `plexos-cloud simulation enqueue gurobi`

**Command Path:** `plexos-cloud → simulation → enqueue → gurobi`

### Help Output

```
CloudCLI.Commands.Simulation.Enqueue.EnqueueGurobiSimulationCommand

(Early Access) Enqueues a Gurobi tuning job. Command is in early access so specific arguments and responses are subject to change.

Usage: plexos-cloud simulation enqueue gurobi [options]

Options:
  -f|--format            Output format(json | csv | tsv | yaml | table | none)
                         Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                         YAML.
                         Default value is: JSON.
  -q|--quiet             Turns off verbose messages from app
  -aut|--automation      Turns on developer friendly structured response
                         messages from app
                         Allowed values are: None, PythonSDK.
  --jsonOnly             Show the created JSON body only, or show the request
                         contract if using just enqueue. Does not enqueue a
                         simulation.
  --studyId              Study ID (required)
  --models               Models (required)
  --engineId             Engine ID (required)
  --changesetId          Changeset ID (optional) (latest changeset from study is
                         default)
  --cpuCores             CPU Cores (required)
  --memoryInGb           Memory in GB (required)
  --locale               Locale (optional) (1033 - en-US - default)
  --parquetVersion       Parquet Version (deprecated) (2 default)
  --simulationDataTypes  Simulation Data Types (optional) (Default is
                         ChangesetDatabase, TimeseriesZipped)
                         Allowed values are: ChangesetDatabase,
                         TimeseriesDatabase, ZippedXmlInput, ZippedExtras,
                         TimeseriesZipped, AncillaryZippedInput, LocalXml,
                         ZippedAuroraInput, ZippedManifests.
  --simulationRunType    Simulation Run Type (optional) (Default is SingleRun)
                         Allowed values are: ModelDistributionRun,
                         MultipleVmSelectionRun, SingleRun.
  --enableSnapshots      Enable PLEXOS Snapshots (optional)
  --snapshotInterval     Snapshot Interval in minutes (--enableSnapshots must be
                         used)
  --exportContractPath   If specified, this will export the enqueue request into
                         a JSON file (enqueueRequest.json) at the specified path
                         (optional)
  --set-context          Set the current context to the new simulation after
                         enqueueing.
  --max-tune-time        Maximum time to spend tuning the model in seconds.
                         (required)
  --tune-trials          Number of trials to run when tuning the model.
                         (required)
  --mip-gap              Maximum MIP gap. (required)
  -?|-h|--help           Show help information.


```

---

## `plexos-cloud simulation enqueue in`

**Command Path:** `plexos-cloud → simulation → enqueue → in`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'in'

```

---

## `plexos-cloud simulation enqueue monte-carlo`

**Command Path:** `plexos-cloud → simulation → enqueue → monte-carlo`

### Help Output

```
CloudCLI.Commands.Simulation.Enqueue.EnqueueMonteCarloSimulationCommand

(Early Access) Enqueues a Monte Carlo (V2) simulation. Command is in early access so specific arguments and responses are subject to change.

Usage: plexos-cloud simulation enqueue monte-carlo [options]

Options:
  -f|--format            Output format(json | csv | tsv | yaml | table | none)
                         Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                         YAML.
                         Default value is: JSON.
  -q|--quiet             Turns off verbose messages from app
  -aut|--automation      Turns on developer friendly structured response
                         messages from app
                         Allowed values are: None, PythonSDK.
  --jsonOnly             Show the created JSON body only, or show the request
                         contract if using just enqueue. Does not enqueue a
                         simulation.
  --studyId              Study ID (required)
  --models               Models (required)
  --engineId             Engine ID (required)
  --changesetId          Changeset ID (optional) (latest changeset from study is
                         default)
  --cpuCores             CPU Cores (required)
  --memoryInGb           Memory in GB (required)
  --locale               Locale (optional) (1033 - en-US - default)
  --parquetVersion       Parquet Version (deprecated) (2 default)
  --simulationDataTypes  Simulation Data Types (optional) (Default is
                         ChangesetDatabase, TimeseriesZipped)
                         Allowed values are: ChangesetDatabase,
                         TimeseriesDatabase, ZippedXmlInput, ZippedExtras,
                         TimeseriesZipped, AncillaryZippedInput, LocalXml,
                         ZippedAuroraInput, ZippedManifests.
  --simulationRunType    Simulation Run Type (optional) (Default is SingleRun)
                         Allowed values are: ModelDistributionRun,
                         MultipleVmSelectionRun, SingleRun.
  --enableSnapshots      Enable PLEXOS Snapshots (optional)
  --snapshotInterval     Snapshot Interval in minutes (--enableSnapshots must be
                         used)
  --exportContractPath   If specified, this will export the enqueue request into
                         a JSON file (enqueueRequest.json) at the specified path
                         (optional)
  --set-context          Set the current context to the new simulation after
                         enqueueing.
  --split-divisions      Number of divisions to split the simulation into.
                         (required)
  --split-type           The split type for the monte carlo simulation.
                         (optional) (UserDefinedSamples is default))
                         Allowed values are: Chronological, Geographical,
                         Planning, Outages, UserDefinedSamples.
  -?|-h|--help           Show help information.


```

---

## `plexos-cloud simulation enqueue responses`

**Command Path:** `plexos-cloud → simulation → enqueue → responses`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'responses'

```

---

## `plexos-cloud simulation enqueue simulation.`

**Command Path:** `plexos-cloud → simulation → enqueue → simulation.`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'simulation.'

```

---

## `plexos-cloud simulation enqueue so`

**Command Path:** `plexos-cloud → simulation → enqueue → so`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'so'

```

---

## `plexos-cloud simulation enqueue standard`

**Command Path:** `plexos-cloud → simulation → enqueue → standard`

### Help Output

```
CloudCLI.Commands.Simulation.Enqueue.EnqueueStandardSimulationCommand

(Early Access) Enqueues a standard simulation in Plexos using arguments. Can also be used as a starting point to build requests with the default type. Command is in early access so specific arguments and responses are subject to change.

Usage: plexos-cloud simulation enqueue standard [options]

Options:
  -f|--format            Output format(json | csv | tsv | yaml | table | none)
                         Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                         YAML.
                         Default value is: JSON.
  -q|--quiet             Turns off verbose messages from app
  -aut|--automation      Turns on developer friendly structured response
                         messages from app
                         Allowed values are: None, PythonSDK.
  --jsonOnly             Show the created JSON body only, or show the request
                         contract if using just enqueue. Does not enqueue a
                         simulation.
  --studyId              Study ID (required)
  --models               Models (required)
  --engineId             Engine ID (required)
  --changesetId          Changeset ID (optional) (latest changeset from study is
                         default)
  --cpuCores             CPU Cores (required)
  --memoryInGb           Memory in GB (required)
  --locale               Locale (optional) (1033 - en-US - default)
  --parquetVersion       Parquet Version (deprecated) (2 default)
  --simulationDataTypes  Simulation Data Types (optional) (Default is
                         ChangesetDatabase, TimeseriesZipped)
                         Allowed values are: ChangesetDatabase,
                         TimeseriesDatabase, ZippedXmlInput, ZippedExtras,
                         TimeseriesZipped, AncillaryZippedInput, LocalXml,
                         ZippedAuroraInput, ZippedManifests.
  --simulationRunType    Simulation Run Type (optional) (Default is SingleRun)
                         Allowed values are: ModelDistributionRun,
                         MultipleVmSelectionRun, SingleRun.
  --enableSnapshots      Enable PLEXOS Snapshots (optional)
  --snapshotInterval     Snapshot Interval in minutes (--enableSnapshots must be
                         used)
  --exportContractPath   If specified, this will export the enqueue request into
                         a JSON file (enqueueRequest.json) at the specified path
                         (optional)
  --set-context          Set the current context to the new simulation after
                         enqueueing.
  -?|-h|--help           Show help information.


```

---

## `plexos-cloud simulation enqueue stochastic`

**Command Path:** `plexos-cloud → simulation → enqueue → stochastic`

### Help Output

```
CloudCLI.Commands.Simulation.Enqueue.EnqueueStochasticSimulationCommand

(Early Access) Enqueues a stochastic (Monte Carlo V1) simulation. Command is in early access so specific arguments and responses are subject to change.

Usage: plexos-cloud simulation enqueue stochastic [options]

Options:
  -f|--format            Output format(json | csv | tsv | yaml | table | none)
                         Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                         YAML.
                         Default value is: JSON.
  -q|--quiet             Turns off verbose messages from app
  -aut|--automation      Turns on developer friendly structured response
                         messages from app
                         Allowed values are: None, PythonSDK.
  --jsonOnly             Show the created JSON body only, or show the request
                         contract if using just enqueue. Does not enqueue a
                         simulation.
  --studyId              Study ID (required)
  --models               Models (required)
  --engineId             Engine ID (required)
  --changesetId          Changeset ID (optional) (latest changeset from study is
                         default)
  --cpuCores             CPU Cores (required)
  --memoryInGb           Memory in GB (required)
  --locale               Locale (optional) (1033 - en-US - default)
  --parquetVersion       Parquet Version (deprecated) (2 default)
  --simulationDataTypes  Simulation Data Types (optional) (Default is
                         ChangesetDatabase, TimeseriesZipped)
                         Allowed values are: ChangesetDatabase,
                         TimeseriesDatabase, ZippedXmlInput, ZippedExtras,
                         TimeseriesZipped, AncillaryZippedInput, LocalXml,
                         ZippedAuroraInput, ZippedManifests.
  --simulationRunType    Simulation Run Type (optional) (Default is SingleRun)
                         Allowed values are: ModelDistributionRun,
                         MultipleVmSelectionRun, SingleRun.
  --enableSnapshots      Enable PLEXOS Snapshots (optional)
  --snapshotInterval     Snapshot Interval in minutes (--enableSnapshots must be
                         used)
  --exportContractPath   If specified, this will export the enqueue request into
                         a JSON file (enqueueRequest.json) at the specified path
                         (optional)
  --set-context          Set the current context to the new simulation after
                         enqueueing.
  --instance-count       Number of instances to run. (required)
  -?|-h|--help           Show help information.


```

---

## `plexos-cloud simulation enqueue subject`

**Command Path:** `plexos-cloud → simulation → enqueue → subject`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'subject'

```

---

## `plexos-cloud simulation enqueue using`

**Command Path:** `plexos-cloud → simulation → enqueue → using`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'using'

```

---

## `plexos-cloud solution bi based`

**Command Path:** `plexos-cloud → solution → bi → based`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'based'

```

---

## `plexos-cloud solution bi delete`

**Command Path:** `plexos-cloud → solution → bi → delete`

### Help Output

```
CloudCLI.Commands.Solution.Bi.DeleteBiCommand

Unpublishes the solution from BI Analytics

Usage: plexos-cloud solution bi delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --solutionId       The solution id (Required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution bi filtered`

**Command Path:** `plexos-cloud → solution → bi → filtered`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'filtered'

```

---

## `plexos-cloud solution bi list`

**Command Path:** `plexos-cloud → solution → bi → list`

### Help Output

```
CloudCLI.Commands.Solution.Bi.ListBiSolutionsCommand

Fetches published solutions from BI Analytics, optionally filtered by study ID.

Usage: plexos-cloud solution bi list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The study id to filter solutions by a specific study.
                     (Optional)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution bi publish`

**Command Path:** `plexos-cloud → solution → bi → publish`

### Help Output

```
CloudCLI.Commands.Solution.Bi.PublishBiCommand

Publishes the solution to BI Analytics

Usage: plexos-cloud solution bi publish [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --solutionId       The solution id (Required)
  --changesetId      The changeset id (No Longer Supported)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution bi status`

**Command Path:** `plexos-cloud → solution → bi → status`

### Help Output

```
CloudCLI.Commands.Solution.Bi.BiStatusCommand

Fetches the status of the solution added in BI Analytics based on SolutionId

Usage: plexos-cloud solution bi status [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --solutionId       The solution id (Required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution convert Objectives,`

**Command Path:** `plexos-cloud → solution → convert → Objectives,`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'Objectives,'

```

---

## `plexos-cloud solution convert condense-file`

**Command Path:** `plexos-cloud → solution → convert → condense-file`

### Help Output

```
CloudCLI.Commands.Solution.Convert.ConvertLPFileToCondensedFileCommand

Converts the given LP/MIP into a smaller lp file with Objectives, constraints, bounds related to a particular period

Usage: plexos-cloud solution convert condense-file [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --lpFilePath          Path to the LP file (required)
  --fileName            File name of the condensed file
  --period              Period to convert (required)
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud solution convert database`

**Command Path:** `plexos-cloud → solution → convert → database`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'database'

```

---

## `plexos-cloud solution convert hybrid-to-parquet`

**Command Path:** `plexos-cloud → solution → convert → hybrid-to-parquet`

### Help Output

```
CloudCLI.Commands.Solution.Convert.ConvertHybridToParquetCommand

Converts the PLEXOS Cloud hybrid (sqlite + parquet) database format to the full parquet database structure

Usage: plexos-cloud solution convert hybrid-to-parquet [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --sqlitePath          Path to the PLEXOS Cloud sqlite database (required)
  --parquetDir          Path to the PLEXOS Cloud parquet data directory files
                        for the hybrid format (required)
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud solution convert of`

**Command Path:** `plexos-cloud → solution → convert → of`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'of'

```

---

## `plexos-cloud solution convert period`

**Command Path:** `plexos-cloud → solution → convert → period`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'period'

```

---

## `plexos-cloud solution convert zip-to-hybrid`

**Command Path:** `plexos-cloud → solution → convert → zip-to-hybrid`

### Help Output

```
CloudCLI.Commands.Solution.Convert.ConvertRawZipToHybridCommand

Converts the PLEXOS zip output database to a hybrid format of sqlite with parquet data

Usage: plexos-cloud solution convert zip-to-hybrid [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --zipPath             Path to the PLEXOS zip output file (required)
  --schemaVersion       Schema version for hybrid output data (deprecated).
                        Default is: 2
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud solution convert zip-to-parquet`

**Command Path:** `plexos-cloud → solution → convert → zip-to-parquet`

### Help Output

```
CloudCLI.Commands.Solution.Convert.ConvertRawZipToParquetCommand

Converts the PLEXOS zip output database to a parquet format

Usage: plexos-cloud solution convert zip-to-parquet [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --zipPath             Path to the PLEXOS zip output file (required)
  --schemaVersion       Schema version for parquet output data (deprecated).
                        Default is: 2
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud solution files download`

**Command Path:** `plexos-cloud → solution → files → download`

### Help Output

```
CloudCLI.Commands.Solution.DownloadSolutionCommand

Download data related to a solution

Usage: plexos-cloud solution files download [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --solutionId          Filter by the solution ID (required)
  --type                Filter by a solution file type. For a list of available
                        file types for a given solution, use the 'solution files
                        list-types' command
  --file                Download specific file by name
  --generateMetaData    Generate meta data file for solution
  --metaDataFileName    Meta data file name
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud solution files list`

**Command Path:** `plexos-cloud → solution → files → list`

### Help Output

```
CloudCLI.Commands.Solution.ListSolutionFilesCommand

List files for a solution

Usage: plexos-cloud solution files list [options]

Options:
  -f|--format              Output format(json | csv | tsv | yaml | table | none)
                           Allowed values are: JSON, JSONL, CSV, None, Table,
                           TSV, YAML.
                           Default value is: JSON.
  -q|--quiet               Turns off verbose messages from app
  -aut|--automation        Turns on developer friendly structured response
                           messages from app
                           Allowed values are: None, PythonSDK.
  --solutionId             Filter by the solution ID (required)
  --type                   Filter by a solution file type. For a list of
                           available file types for a given solution, use the
                           'solution files list-types' command
  --includeArchiveEntries  List the files inside of zipped archives
  -?|-h|--help             Show help information.


```

---

## `plexos-cloud solution files list-types`

**Command Path:** `plexos-cloud → solution → files → list-types`

### Help Output

```
CloudCLI.Commands.Solution.ListSolutionFileTypesCommand

List available file types for a solution

Usage: plexos-cloud solution files list-types [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --solutionId       List file types by the solution ID (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution query configure-views`

**Command Path:** `plexos-cloud → solution → query → configure-views`

### Help Output

```
CloudCLI.Commands.Solution.ConfigureViewsCommand

Configures DuckDb views to simplify parquet querying by model

Usage: plexos-cloud solution query configure-views [options]

Options:
  -f|--format         Output format(json | csv | tsv | yaml | table | none)
                      Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                      YAML.
                      Default value is: JSON.
  -q|--quiet          Turns off verbose messages from app
  -aut|--automation   Turns on developer friendly structured response messages
                      from app
                      Allowed values are: None, PythonSDK.
  -n|--model-name     Model name for solution data (Required)
  -m|--map-path       Json map file path
                      Default value is:
                      C:\Users\alejandro.elenes\Documents\techprogress
                      POC\directorymapping.desktop.json.
  -d|--database-path  Duck database path - Used to persist views and schema for
                      automation (Required)
  -?|-h|--help        Show help information.


```

---

## `plexos-cloud solution query model`

**Command Path:** `plexos-cloud → solution → query → model`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'model'

```

---

## `plexos-cloud solution view for`

**Command Path:** `plexos-cloud → solution → view → for`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'for'

```

---

## `plexos-cloud solution view get-downloadable-report-details`

**Command Path:** `plexos-cloud → solution → view → get-downloadable-report-details`

### Help Output

```
CloudCLI.Commands.Solution.View.GetViewReportsDetailsCommand

Get view report details along with commands for all the reports in View for downloading report data

Usage: plexos-cloud solution view get-downloadable-report-details [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --viewId           ID of the view (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution view get-report-data`

**Command Path:** `plexos-cloud → solution → view → get-report-data`

### Help Output

```
CloudCLI.Commands.Solution.View.GetSolutionDataUsingViewCommand

Get solution report data

Usage: plexos-cloud solution view get-report-data [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  -d|--outputDirectory  Directory for command output to be written to (required)
  --overwrite           Overwrite any file that already exists
  --solutionId          Solution ID (required)
  --reportId            ID of the report (required)
  --viewId              ID of the view (required)
  --file                File name (required)
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud solution view list`

**Command Path:** `plexos-cloud → solution → view → list`

### Help Output

```
CloudCLI.Commands.Solution.View.ListViewsCommand

List of assigned views

Usage: plexos-cloud solution view list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution view publish`

**Command Path:** `plexos-cloud → solution → view → publish`

### Help Output

```
CloudCLI.Commands.Solution.View.PublishViewCommand

Publish a view

Usage: plexos-cloud solution view publish [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --file             Path to the configuration file
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud solution view report`

**Command Path:** `plexos-cloud → solution → view → report`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'report'

```

---

## `plexos-cloud study changeset are`

**Command Path:** `plexos-cloud → study → changeset → are`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'are'

```

---

## `plexos-cloud study changeset building`

**Command Path:** `plexos-cloud → study → changeset → building`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'building'

```

---

## `plexos-cloud study changeset download`

**Command Path:** `plexos-cloud → study → changeset → download`

### Help Output

```
CloudCLI.Commands.Study.Changesets.DownloadSpecificChangesetCommand

Downloads XML and timeseries (if applicable) files for a study's changeset. Changes to these files will not be tracked by the study by default.

Usage: plexos-cloud study changeset download [options]

Options:
  -f|--format           Output format(json | csv | tsv | yaml | table | none)
                        Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                        YAML.
                        Default value is: JSON.
  -q|--quiet            Turns off verbose messages from app
  -aut|--automation     Turns on developer friendly structured response messages
                        from app
                        Allowed values are: None, PythonSDK.
  --studyId             The ID of the study (required)
  --changesetId         The ID of the changeset (required)
  -o|--outputDirectory  Directory for command output to be written to (required)
  --listFiles           List the files that were downloaded and converted from
                        the download.
  -?|-h|--help          Show help information.


```

---

## `plexos-cloud study changeset get-latest`

**Command Path:** `plexos-cloud → study → changeset → get-latest`

### Help Output

```
CloudCLI.Commands.Study.Changesets.GetLastChangesetIdCommand

Gets Latest Changeset ID for Study.

Usage: plexos-cloud study changeset get-latest [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset get-latest-local`

**Command Path:** `plexos-cloud → study → changeset → get-latest-local`

### Help Output

```
CloudCLI.Commands.Study.Changesets.GetLastLocalChangesetIdCommand

Gets Latest Local Changeset ID for Study.

Usage: plexos-cloud study changeset get-latest-local [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset get-status`

**Command Path:** `plexos-cloud → study → changeset → get-status`

### Help Output

```
CloudCLI.Commands.Study.Changesets.GetChangesetStatusCommand

Fetches the changeset status of the current study, if there are incoming/outgoing changesets or the study is in sync

Usage: plexos-cloud study changeset get-status [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset get-urls`

**Command Path:** `plexos-cloud → study → changeset → get-urls`

### Help Output

```
CloudCLI.Commands.Study.GetChangesetDownloadUrlsCommand

List the download URLS for this changeset. Only used for building a simulation enqueue request for this changeset, using the URLS still requires API authentication

Usage: plexos-cloud study changeset get-urls [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          Filter by the study ID (required)
  --changesetId      Filter by the changeset ID (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset list`

**Command Path:** `plexos-cloud → study → changeset → list`

### Help Output

```
CloudCLI.Commands.Study.Changesets.ListChangesetsCommand

List the changesets for a study

Usage: plexos-cloud study changeset list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset list-local`

**Command Path:** `plexos-cloud → study → changeset → list-local`

### Help Output

```
CloudCLI.Commands.Study.Changesets.ListLocalChangesetsCommand

List the local changesets for a study

Usage: plexos-cloud study changeset list-local [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset pull`

**Command Path:** `plexos-cloud → study → changeset → pull`

### Help Output

```
CloudCLI.Commands.Study.Changesets.PullLatestCommand

Pull the latest changes for a study

Usage: plexos-cloud study changeset pull [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset push`

**Command Path:** `plexos-cloud → study → changeset → push`

### Help Output

```
CloudCLI.Commands.Study.Changesets.PushChangesCommand

Push the latest changes for a study

Usage: plexos-cloud study changeset push [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --message          A short message for the commit (required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study changeset study's`

**Command Path:** `plexos-cloud → study → changeset → study's`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'study's'

```

---

## `plexos-cloud study changeset tracked`

**Command Path:** `plexos-cloud → study → changeset → tracked`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'tracked'

```

---

## `plexos-cloud study changeset using`

**Command Path:** `plexos-cloud → study → changeset → using`

### Help Output

```
Error (exit code 1): Error: Unrecognized command or argument 'using'

```

---

## `plexos-cloud study settings add-configurations`

**Command Path:** `plexos-cloud → study → settings → add-configurations`

### Help Output

```
CloudCLI.Commands.Study.Settings.AddConfigurationsCommand

Add configurations to the existing study settings

Usage: plexos-cloud study settings add-configurations [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The study identifier. (Required)
  --settingId        The study settings identifier. (Required)
  -t|--type          The study settings type. Example SimulationGroup.
                     (Required)
  -p|--path          The study settings configuration payload file path,
                     Supported format - json. (Required)
  --showExample      Show an example configuration file template
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study settings create`

**Command Path:** `plexos-cloud → study → settings → create`

### Help Output

```
CloudCLI.Commands.Study.Settings.CreateSettingsCommand

create study settings based on settings type.

Usage: plexos-cloud study settings create [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The study identifier. (Required)
  -t|--type          The study settings type. Example SimulationGroup.
                     (Required)
  -p|--path          The study settings payload file path, Supported format -
                     json. (Required)
  --showExample      Show an example configuration file template
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study settings delete`

**Command Path:** `plexos-cloud → study → settings → delete`

### Help Output

```
CloudCLI.Commands.Study.Settings.DeleteSettingsCommand

Delete the study settings

Usage: plexos-cloud study settings delete [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --settingId        List of study setting IDs to be deleted
                     :studySettingId1,studySettingId2 (Required)
  --studyId          The study identifier. (Required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study settings list`

**Command Path:** `plexos-cloud → study → settings → list`

### Help Output

```
CloudCLI.Commands.Study.Settings.ListSettingsCommand

List the study settings available for the given study

Usage: plexos-cloud study settings list [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The study identifier. (Required)
  -?|-h|--help       Show help information.


```

---

## `plexos-cloud study stats geocoded-objects`

**Command Path:** `plexos-cloud → study → stats → geocoded-objects`

### Help Output

```
CloudCLI.Commands.Study.StudyStats.GetGeoCodedObjectsCommand

Number of geocoded Objects

Usage: plexos-cloud study stats geocoded-objects [options]

Options:
  -f|--format        Output format(json | csv | tsv | yaml | table | none)
                     Allowed values are: JSON, JSONL, CSV, None, Table, TSV,
                     YAML.
                     Default value is: JSON.
  -q|--quiet         Turns off verbose messages from app
  -aut|--automation  Turns on developer friendly structured response messages
                     from app
                     Allowed values are: None, PythonSDK.
  --studyId          The ID of the study (required)
  --changesetId      The ID of the changeSet (required)
  -?|-h|--help       Show help information.


```

---


---

## 📊 Documentation Statistics

- **Total Commands Documented:** 206
- **CLI Tool:** `plexos-cloud`
- **Generated By:** PLEXOS CLI Documentation Generator
