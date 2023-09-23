"""
    pygments.lexers._mysql_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Self-updating data files for the MySQL lexer.

    Run with `python -I` to update.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""


MYSQL_CONSTANTS = (
    'false',
    'null',
    'true',
    'unknown',
)


# At this time, no easily-parsed, definitive list of data types
# has been found in the MySQL source code or documentation. (The
# `sql/sql_yacc.yy` file is definitive but is difficult to parse.)
# Therefore these types are currently maintained manually.
#
# Some words in this list -- like "long", "national", "precision",
# and "varying" -- appear to only occur in combination with other
# data type keywords. Therefore they are included as separate words
# even though they do not naturally occur in syntax separately.
#
# This list is also used to strip data types out of the list of
# MySQL keywords, which is automatically updated later in the file.
#
MYSQL_DATATYPES = (
    # Numeric data types
    'bigint',
    'bit',
    'bool',
    'boolean',
    'dec',
    'decimal',
    'double',
    'fixed',
    'float',
    'float4',
    'float8',
    'int',
    'int1',
    'int2',
    'int3',
    'int4',
    'int8',
    'integer',
    'mediumint',
    'middleint',
    'numeric',
    'precision',
    'real',
    'serial',
    'smallint',
    'tinyint',

    # Date and time data types
    'date',
    'datetime',
    'time',
    'timestamp',
    'year',

    # String data types
    'binary',
    'blob',
    'char',
    'enum',
    'long',
    'longblob',
    'longtext',
    'mediumblob',
    'mediumtext',
    'national',
    'nchar',
    'nvarchar',
    'set',
    'text',
    'tinyblob',
    'tinytext',
    'varbinary',
    'varchar',
    'varcharacter',
    'varying',

    # Spatial data types
    'geometry',
    'geometrycollection',
    'linestring',
    'multilinestring',
    'multipoint',
    'multipolygon',
    'point',
    'polygon',

    # JSON data types
    'json',
)

# Everything below this line is auto-generated from the MySQL source code.
# Run this file in Python and it will update itself.
# -----------------------------------------------------------------------------

MYSQL_FUNCTIONS = (
    'abs',
    'acos',
    'adddate',
    'addtime',
    'aes_decrypt',
    'aes_encrypt',
    'any_value',
    'asin',
    'atan',
    'atan2',
    'benchmark',
    'bin',
    'bin_to_uuid',
    'bit_and',
    'bit_count',
    'bit_length',
    'bit_or',
    'bit_xor',
    'can_access_column',
    'can_access_database',
    'can_access_event',
    'can_access_resource_group',
    'can_access_routine',
    'can_access_table',
    'can_access_trigger',
    'can_access_user',
    'can_access_view',
    'cast',
    'ceil',
    'ceiling',
    'char_length',
    'character_length',
    'coercibility',
    'compress',
    'concat',
    'concat_ws',
    'connection_id',
    'conv',
    'convert_cpu_id_mask',
    'convert_interval_to_user_interval',
    'convert_tz',
    'cos',
    'cot',
    'count',
    'crc32',
    'curdate',
    'current_role',
    'curtime',
    'date_add',
    'date_format',
    'date_sub',
    'datediff',
    'dayname',
    'dayofmonth',
    'dayofweek',
    'dayofyear',
    'degrees',
    'elt',
    'exp',
    'export_set',
    'extract',
    'extractvalue',
    'field',
    'find_in_set',
    'floor',
    'format_bytes',
    'format_pico_time',
    'found_rows',
    'from_base64',
    'from_days',
    'from_unixtime',
    'get_dd_column_privileges',
    'get_dd_create_options',
    'get_dd_index_private_data',
    'get_dd_index_sub_part_length',
    'get_dd_property_key_value',
    'get_dd_schema_options',
    'get_dd_tablespace_private_data',
    'get_lock',
    'greatest',
    'group_concat',
    'gtid_subset',
    'gtid_subtract',
    'hex',
    'icu_version',
    'ifnull',
    'inet6_aton',
    'inet6_ntoa',
    'inet_aton',
    'inet_ntoa',
    'instr',
    'internal_auto_increment',
    'internal_avg_row_length',
    'internal_check_time',
    'internal_checksum',
    'internal_data_free',
    'internal_data_length',
    'internal_dd_char_length',
    'internal_get_comment_or_error',
    'internal_get_dd_column_extra',
    'internal_get_enabled_role_json',
    'internal_get_hostname',
    'internal_get_mandatory_roles_json',
    'internal_get_partition_nodegroup',
    'internal_get_username',
    'internal_get_view_warning_or_error',
    'internal_index_column_cardinality',
    'internal_index_length',
    'internal_is_enabled_role',
    'internal_is_mandatory_role',
    'internal_keys_disabled',
    'internal_max_data_length',
    'internal_table_rows',
    'internal_tablespace_autoextend_size',
    'internal_tablespace_data_free',
    'internal_tablespace_extent_size',
    'internal_tablespace_extra',
    'internal_tablespace_free_extents',
    'internal_tablespace_id',
    'internal_tablespace_initial_size',
    'internal_tablespace_logfile_group_name',
    'internal_tablespace_logfile_group_number',
    'internal_tablespace_maximum_size',
    'internal_tablespace_row_format',
    'internal_tablespace_status',
    'internal_tablespace_total_extents',
    'internal_tablespace_type',
    'internal_tablespace_version',
    'internal_update_time',
    'is_free_lock',
    'is_ipv4',
    'is_ipv4_compat',
    'is_ipv4_mapped',
    'is_ipv6',
    'is_used_lock',
    'is_uuid',
    'is_visible_dd_object',
    'isnull',
    'json_array',
    'json_array_append',
    'json_array_insert',
    'json_arrayagg',
    'json_contains',
    'json_contains_path',
    'json_depth',
    'json_extract',
    'json_insert',
    'json_keys',
    'json_length',
    'json_merge',
    'json_merge_patch',
    'json_merge_preserve',
    'json_object',
    'json_objectagg',
    'json_overlaps',
    'json_pretty',
    'json_quote',
    'json_remove',
    'json_replace',
    'json_schema_valid',
    'json_schema_validation_report',
    'json_search',
    'json_set',
    'json_storage_free',
    'json_storage_size',
    'json_type',
    'json_unquote',
    'json_valid',
    'last_day',
    'last_insert_id',
    'lcase',
    'least',
    'length',
    'like_range_max',
    'like_range_min',
    'ln',
    'load_file',
    'locate',
    'log',
    'log10',
    'log2',
    'lower',
    'lpad',
    'ltrim',
    'make_set',
    'makedate',
    'maketime',
    'master_pos_wait',
    'max',
    'mbrcontains',
    'mbrcoveredby',
    'mbrcovers',
    'mbrdisjoint',
    'mbrequals',
    'mbrintersects',
    'mbroverlaps',
    'mbrtouches',
    'mbrwithin',
    'md5',
    'mid',
    'min',
    'monthname',
    'name_const',
    'now',
    'nullif',
    'oct',
    'octet_length',
    'ord',
    'period_add',
    'period_diff',
    'pi',
    'position',
    'pow',
    'power',
    'ps_current_thread_id',
    'ps_thread_id',
    'quote',
    'radians',
    'rand',
    'random_bytes',
    'regexp_instr',
    'regexp_like',
    'regexp_replace',
    'regexp_substr',
    'release_all_locks',
    'release_lock',
    'remove_dd_property_key',
    'reverse',
    'roles_graphml',
    'round',
    'rpad',
    'rtrim',
    'sec_to_time',
    'session_user',
    'sha',
    'sha1',
    'sha2',
    'sign',
    'sin',
    'sleep',
    'soundex',
    'source_pos_wait',
    'space',
    'sqrt',
    'st_area',
    'st_asbinary',
    'st_asgeojson',
    'st_astext',
    'st_aswkb',
    'st_aswkt',
    'st_buffer',
    'st_buffer_strategy',
    'st_centroid',
    'st_collect',
    'st_contains',
    'st_convexhull',
    'st_crosses',
    'st_difference',
    'st_dimension',
    'st_disjoint',
    'st_distance',
    'st_distance_sphere',
    'st_endpoint',
    'st_envelope',
    'st_equals',
    'st_exteriorring',
    'st_frechetdistance',
    'st_geohash',
    'st_geomcollfromtext',
    'st_geomcollfromtxt',
    'st_geomcollfromwkb',
    'st_geometrycollectionfromtext',
    'st_geometrycollectionfromwkb',
    'st_geometryfromtext',
    'st_geometryfromwkb',
    'st_geometryn',
    'st_geometrytype',
    'st_geomfromgeojson',
    'st_geomfromtext',
    'st_geomfromwkb',
    'st_hausdorffdistance',
    'st_interiorringn',
    'st_intersection',
    'st_intersects',
    'st_isclosed',
    'st_isempty',
    'st_issimple',
    'st_isvalid',
    'st_latfromgeohash',
    'st_latitude',
    'st_length',
    'st_linefromtext',
    'st_linefromwkb',
    'st_lineinterpolatepoint',
    'st_lineinterpolatepoints',
    'st_linestringfromtext',
    'st_linestringfromwkb',
    'st_longfromgeohash',
    'st_longitude',
    'st_makeenvelope',
    'st_mlinefromtext',
    'st_mlinefromwkb',
    'st_mpointfromtext',
    'st_mpointfromwkb',
    'st_mpolyfromtext',
    'st_mpolyfromwkb',
    'st_multilinestringfromtext',
    'st_multilinestringfromwkb',
    'st_multipointfromtext',
    'st_multipointfromwkb',
    'st_multipolygonfromtext',
    'st_multipolygonfromwkb',
    'st_numgeometries',
    'st_numinteriorring',
    'st_numinteriorrings',
    'st_numpoints',
    'st_overlaps',
    'st_pointatdistance',
    'st_pointfromgeohash',
    'st_pointfromtext',
    'st_pointfromwkb',
    'st_pointn',
    'st_polyfromtext',
    'st_polyfromwkb',
    'st_polygonfromtext',
    'st_polygonfromwkb',
    'st_simplify',
    'st_srid',
    'st_startpoint',
    'st_swapxy',
    'st_symdifference',
    'st_touches',
    'st_transform',
    'st_union',
    'st_validate',
    'st_within',
    'st_x',
    'st_y',
    'statement_digest',
    'statement_digest_text',
    'std',
    'stddev',
    'stddev_pop',
    'stddev_samp',
    'str_to_date',
    'strcmp',
    'subdate',
    'substr',
    'substring',
    'substring_index',
    'subtime',
    'sum',
    'sysdate',
    'system_user',
    'tan',
    'time_format',
    'time_to_sec',
    'timediff',
    'to_base64',
    'to_days',
    'to_seconds',
    'trim',
    'ucase',
    'uncompress',
    'uncompressed_length',
    'unhex',
    'unix_timestamp',
    'updatexml',
    'upper',
    'uuid',
    'uuid_short',
    'uuid_to_bin',
    'validate_password_strength',
    'var_pop',
    'var_samp',
    'variance',
    'version',
    'wait_for_executed_gtid_set',
    'wait_until_sql_thread_after_gtids',
    'weekday',
    'weekofyear',
    'yearweek',
)


MYSQL_OPTIMIZER_HINTS = (
    'bka',
    'bnl',
    'derived_condition_pushdown',
    'dupsweedout',
    'firstmatch',
    'group_index',
    'hash_join',
    'index',
    'index_merge',
    'intoexists',
    'join_fixed_order',
    'join_index',
    'join_order',
    'join_prefix',
    'join_suffix',
    'loosescan',
    'materialization',
    'max_execution_time',
    'merge',
    'mrr',
    'no_bka',
    'no_bnl',
    'no_derived_condition_pushdown',
    'no_group_index',
    'no_hash_join',
    'no_icp',
    'no_index',
    'no_index_merge',
    'no_join_index',
    'no_merge',
    'no_mrr',
    'no_order_index',
    'no_range_optimization',
    'no_semijoin',
    'no_skip_scan',
    'order_index',
    'qb_name',
    'resource_group',
    'semijoin',
    'set_var',
    'skip_scan',
    'subquery',
)


MYSQL_KEYWORDS = (
    'accessible',
    'account',
    'action',
    'active',
    'add',
    'admin',
    'after',
    'against',
    'aggregate',
    'algorithm',
    'all',
    'alter',
    'always',
    'analyze',
    'and',
    'any',
    'array',
    'as',
    'asc',
    'ascii',
    'asensitive',
    'assign_gtids_to_anonymous_transactions',
    'at',
    'attribute',
    'authentication',
    'auto_increment',
    'autoextend_size',
    'avg',
    'avg_row_length',
    'backup',
    'before',
    'begin',
    'between',
    'binlog',
    'block',
    'both',
    'btree',
    'buckets',
    'by',
    'byte',
    'cache',
    'call',
    'cascade',
    'cascaded',
    'case',
    'catalog_name',
    'chain',
    'challenge_response',
    'change',
    'changed',
    'channel',
    'character',
    'charset',
    'check',
    'checksum',
    'cipher',
    'class_origin',
    'client',
    'clone',
    'close',
    'coalesce',
    'code',
    'collate',
    'collation',
    'column',
    'column_format',
    'column_name',
    'columns',
    'comment',
    'commit',
    'committed',
    'compact',
    'completion',
    'component',
    'compressed',
    'compression',
    'concurrent',
    'condition',
    'connection',
    'consistent',
    'constraint',
    'constraint_catalog',
    'constraint_name',
    'constraint_schema',
    'contains',
    'context',
    'continue',
    'convert',
    'cpu',
    'create',
    'cross',
    'cube',
    'cume_dist',
    'current',
    'current_date',
    'current_time',
    'current_timestamp',
    'current_user',
    'cursor',
    'cursor_name',
    'data',
    'database',
    'databases',
    'datafile',
    'day',
    'day_hour',
    'day_microsecond',
    'day_minute',
    'day_second',
    'deallocate',
    'declare',
    'default',
    'default_auth',
    'definer',
    'definition',
    'delay_key_write',
    'delayed',
    'delete',
    'dense_rank',
    'desc',
    'describe',
    'description',
    'deterministic',
    'diagnostics',
    'directory',
    'disable',
    'discard',
    'disk',
    'distinct',
    'distinctrow',
    'div',
    'do',
    'drop',
    'dual',
    'dumpfile',
    'duplicate',
    'dynamic',
    'each',
    'else',
    'elseif',
    'empty',
    'enable',
    'enclosed',
    'encryption',
    'end',
    'ends',
    'enforced',
    'engine',
    'engine_attribute',
    'engines',
    'error',
    'errors',
    'escape',
    'escaped',
    'event',
    'events',
    'every',
    'except',
    'exchange',
    'exclude',
    'execute',
    'exists',
    'exit',
    'expansion',
    'expire',
    'explain',
    'export',
    'extended',
    'extent_size',
    'factor',
    'failed_login_attempts',
    'false',
    'fast',
    'faults',
    'fetch',
    'fields',
    'file',
    'file_block_size',
    'filter',
    'finish',
    'first',
    'first_value',
    'flush',
    'following',
    'follows',
    'for',
    'force',
    'foreign',
    'format',
    'found',
    'from',
    'full',
    'fulltext',
    'function',
    'general',
    'generated',
    'geomcollection',
    'get',
    'get_format',
    'get_master_public_key',
    'get_source_public_key',
    'global',
    'grant',
    'grants',
    'group',
    'group_replication',
    'grouping',
    'groups',
    'gtid_only',
    'handler',
    'hash',
    'having',
    'help',
    'high_priority',
    'histogram',
    'history',
    'host',
    'hosts',
    'hour',
    'hour_microsecond',
    'hour_minute',
    'hour_second',
    'identified',
    'if',
    'ignore',
    'ignore_server_ids',
    'import',
    'in',
    'inactive',
    'index',
    'indexes',
    'infile',
    'initial',
    'initial_size',
    'initiate',
    'inner',
    'inout',
    'insensitive',
    'insert',
    'insert_method',
    'install',
    'instance',
    'interval',
    'into',
    'invisible',
    'invoker',
    'io',
    'io_after_gtids',
    'io_before_gtids',
    'io_thread',
    'ipc',
    'is',
    'isolation',
    'issuer',
    'iterate',
    'join',
    'json_table',
    'json_value',
    'key',
    'key_block_size',
    'keyring',
    'keys',
    'kill',
    'lag',
    'language',
    'last',
    'last_value',
    'lateral',
    'lead',
    'leading',
    'leave',
    'leaves',
    'left',
    'less',
    'level',
    'like',
    'limit',
    'linear',
    'lines',
    'list',
    'load',
    'local',
    'localtime',
    'localtimestamp',
    'lock',
    'locked',
    'locks',
    'logfile',
    'logs',
    'loop',
    'low_priority',
    'master',
    'master_auto_position',
    'master_bind',
    'master_compression_algorithms',
    'master_connect_retry',
    'master_delay',
    'master_heartbeat_period',
    'master_host',
    'master_log_file',
    'master_log_pos',
    'master_password',
    'master_port',
    'master_public_key_path',
    'master_retry_count',
    'master_ssl',
    'master_ssl_ca',
    'master_ssl_capath',
    'master_ssl_cert',
    'master_ssl_cipher',
    'master_ssl_crl',
    'master_ssl_crlpath',
    'master_ssl_key',
    'master_ssl_verify_server_cert',
    'master_tls_ciphersuites',
    'master_tls_version',
    'master_user',
    'master_zstd_compression_level',
    'match',
    'max_connections_per_hour',
    'max_queries_per_hour',
    'max_rows',
    'max_size',
    'max_updates_per_hour',
    'max_user_connections',
    'maxvalue',
    'medium',
    'member',
    'memory',
    'merge',
    'message_text',
    'microsecond',
    'migrate',
    'min_rows',
    'minute',
    'minute_microsecond',
    'minute_second',
    'mod',
    'mode',
    'modifies',
    'modify',
    'month',
    'mutex',
    'mysql_errno',
    'name',
    'names',
    'natural',
    'ndb',
    'ndbcluster',
    'nested',
    'network_namespace',
    'never',
    'new',
    'next',
    'no',
    'no_wait',
    'no_write_to_binlog',
    'nodegroup',
    'none',
    'not',
    'nowait',
    'nth_value',
    'ntile',
    'null',
    'nulls',
    'number',
    'of',
    'off',
    'offset',
    'oj',
    'old',
    'on',
    'one',
    'only',
    'open',
    'optimize',
    'optimizer_costs',
    'option',
    'optional',
    'optionally',
    'options',
    'or',
    'order',
    'ordinality',
    'organization',
    'others',
    'out',
    'outer',
    'outfile',
    'over',
    'owner',
    'pack_keys',
    'page',
    'parser',
    'partial',
    'partition',
    'partitioning',
    'partitions',
    'password',
    'password_lock_time',
    'path',
    'percent_rank',
    'persist',
    'persist_only',
    'phase',
    'plugin',
    'plugin_dir',
    'plugins',
    'port',
    'precedes',
    'preceding',
    'prepare',
    'preserve',
    'prev',
    'primary',
    'privilege_checks_user',
    'privileges',
    'procedure',
    'process',
    'processlist',
    'profile',
    'profiles',
    'proxy',
    'purge',
    'quarter',
    'query',
    'quick',
    'random',
    'range',
    'rank',
    'read',
    'read_only',
    'read_write',
    'reads',
    'rebuild',
    'recover',
    'recursive',
    'redo_buffer_size',
    'redundant',
    'reference',
    'references',
    'regexp',
    'registration',
    'relay',
    'relay_log_file',
    'relay_log_pos',
    'relay_thread',
    'relaylog',
    'release',
    'reload',
    'remove',
    'rename',
    'reorganize',
    'repair',
    'repeat',
    'repeatable',
    'replace',
    'replica',
    'replicas',
    'replicate_do_db',
    'replicate_do_table',
    'replicate_ignore_db',
    'replicate_ignore_table',
    'replicate_rewrite_db',
    'replicate_wild_do_table',
    'replicate_wild_ignore_table',
    'replication',
    'require',
    'require_row_format',
    'require_table_primary_key_check',
    'reset',
    'resignal',
    'resource',
    'respect',
    'restart',
    'restore',
    'restrict',
    'resume',
    'retain',
    'return',
    'returned_sqlstate',
    'returning',
    'returns',
    'reuse',
    'reverse',
    'revoke',
    'right',
    'rlike',
    'role',
    'rollback',
    'rollup',
    'rotate',
    'routine',
    'row',
    'row_count',
    'row_format',
    'row_number',
    'rows',
    'rtree',
    'savepoint',
    'schedule',
    'schema',
    'schema_name',
    'schemas',
    'second',
    'second_microsecond',
    'secondary',
    'secondary_engine',
    'secondary_engine_attribute',
    'secondary_load',
    'secondary_unload',
    'security',
    'select',
    'sensitive',
    'separator',
    'serializable',
    'server',
    'session',
    'share',
    'show',
    'shutdown',
    'signal',
    'signed',
    'simple',
    'skip',
    'slave',
    'slow',
    'snapshot',
    'socket',
    'some',
    'soname',
    'sounds',
    'source',
    'source_auto_position',
    'source_bind',
    'source_compression_algorithms',
    'source_connect_retry',
    'source_connection_auto_failover',
    'source_delay',
    'source_heartbeat_period',
    'source_host',
    'source_log_file',
    'source_log_pos',
    'source_password',
    'source_port',
    'source_public_key_path',
    'source_retry_count',
    'source_ssl',
    'source_ssl_ca',
    'source_ssl_capath',
    'source_ssl_cert',
    'source_ssl_cipher',
    'source_ssl_crl',
    'source_ssl_crlpath',
    'source_ssl_key',
    'source_ssl_verify_server_cert',
    'source_tls_ciphersuites',
    'source_tls_version',
    'source_user',
    'source_zstd_compression_level',
    'spatial',
    'specific',
    'sql',
    'sql_after_gtids',
    'sql_after_mts_gaps',
    'sql_before_gtids',
    'sql_big_result',
    'sql_buffer_result',
    'sql_calc_found_rows',
    'sql_no_cache',
    'sql_small_result',
    'sql_thread',
    'sql_tsi_day',
    'sql_tsi_hour',
    'sql_tsi_minute',
    'sql_tsi_month',
    'sql_tsi_quarter',
    'sql_tsi_second',
    'sql_tsi_week',
    'sql_tsi_year',
    'sqlexception',
    'sqlstate',
    'sqlwarning',
    'srid',
    'ssl',
    'stacked',
    'start',
    'starting',
    'starts',
    'stats_auto_recalc',
    'stats_persistent',
    'stats_sample_pages',
    'status',
    'stop',
    'storage',
    'stored',
    'straight_join',
    'stream',
    'string',
    'subclass_origin',
    'subject',
    'subpartition',
    'subpartitions',
    'super',
    'suspend',
    'swaps',
    'switches',
    'system',
    'table',
    'table_checksum',
    'table_name',
    'tables',
    'tablespace',
    'temporary',
    'temptable',
    'terminated',
    'than',
    'then',
    'thread_priority',
    'ties',
    'timestampadd',
    'timestampdiff',
    'tls',
    'to',
    'trailing',
    'transaction',
    'trigger',
    'triggers',
    'true',
    'truncate',
    'type',
    'types',
    'unbounded',
    'uncommitted',
    'undefined',
    'undo',
    'undo_buffer_size',
    'undofile',
    'unicode',
    'uninstall',
    'union',
    'unique',
    'unknown',
    'unlock',
    'unregister',
    'unsigned',
    'until',
    'update',
    'upgrade',
    'usage',
    'use',
    'use_frm',
    'user',
    'user_resources',
    'using',
    'utc_date',
    'utc_time',
    'utc_timestamp',
    'validation',
    'value',
    'values',
    'variables',
    'vcpu',
    'view',
    'virtual',
    'visible',
    'wait',
    'warnings',
    'week',
    'weight_string',
    'when',
    'where',
    'while',
    'window',
    'with',
    'without',
    'work',
    'wrapper',
    'write',
    'x509',
    'xa',
    'xid',
    'xml',
    'xor',
    'year_month',
    'zerofill',
    'zone',
)


if __name__ == '__main__':  # pragma: no cover
    import re
    from urllib.request import urlopen

    from pygments.util import format_lines

    # MySQL source code
    SOURCE_URL = 'https://github.com/mysql/mysql-server/raw/8.0'
    LEX_URL = SOURCE_URL + '/sql/lex.h'
    ITEM_CREATE_URL = SOURCE_URL + '/sql/item_create.cc'


    def update_myself():
        # Pull content from lex.h.
        lex_file = urlopen(LEX_URL).read().decode('utf8', errors='ignore')
        keywords = parse_lex_keywords(lex_file)
        functions = parse_lex_functions(lex_file)
        optimizer_hints = parse_lex_optimizer_hints(lex_file)

        # Parse content in item_create.cc.
        item_create_file = urlopen(ITEM_CREATE_URL).read().decode('utf8', errors='ignore')
        functions.update(parse_item_create_functions(item_create_file))

        # Remove data types from the set of keywords.
        keywords -= set(MYSQL_DATATYPES)

        update_content('MYSQL_FUNCTIONS', tuple(sorted(functions)))
        update_content('MYSQL_KEYWORDS', tuple(sorted(keywords)))
        update_content('MYSQL_OPTIMIZER_HINTS', tuple(sorted(optimizer_hints)))


    def parse_lex_keywords(f):
        """Parse keywords in lex.h."""

        if results := {
            m.group('keyword').lower()
            for m in re.finditer(
                r'{SYM(?:_HK)?\("(?P<keyword>[a-z0-9_]+)",', f, flags=re.I
            )
        }:
            return results
        else:
            raise ValueError('No keywords found')


    def parse_lex_optimizer_hints(f):
        """Parse optimizer hints in lex.h."""

        if results := {
            m.group('keyword').lower()
            for m in re.finditer(
                r'{SYM_H\("(?P<keyword>[a-z0-9_]+)",', f, flags=re.I
            )
        }:
            return results
        else:
            raise ValueError('No optimizer hints found')


    def parse_lex_functions(f):
        """Parse MySQL function names from lex.h."""

        if results := {
            m.group('function').lower()
            for m in re.finditer(
                r'{SYM_FN?\("(?P<function>[a-z0-9_]+)",', f, flags=re.I
            )
        }:
            return results
        else:
            raise ValueError('No lex functions found')


    def parse_item_create_functions(f):
        """Parse MySQL function names from item_create.cc."""

        if results := {
            m.group('function').lower()
            for m in re.finditer(
                r'{"(?P<function>[^"]+?)",\s*SQL_F[^(]+?\(', f, flags=re.I
            )
        }:
            return results
        else:
            raise ValueError('No item_create functions found')


    def update_content(field_name, content):
        """Overwrite this file with content parsed from MySQL's source code."""

        with open(__file__) as f:
            data = f.read()

        # Line to start/end inserting
        re_match = re.compile(r'^%s\s*=\s*\($.*?^\s*\)$' % field_name, re.M | re.S)
        m = re_match.search(data)
        if not m:
            raise ValueError(f'Could not find an existing definition for {field_name}')

        new_block = format_lines(field_name, content)
        data = data[:m.start()] + new_block + data[m.end():]

        with open(__file__, 'w', newline='\n') as f:
            f.write(data)

    update_myself()
