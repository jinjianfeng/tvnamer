#!/usr/bin/env python
#encoding:utf-8
#author:dbr/Ben
#project:tvnamer
#repository:http://github.com/dbr/tvnamer
#license:Creative Commons GNU GPL v2
# http://creativecommons.org/licenses/GPL/2.0/

"""Holds default config values
"""

defaults = {
    # Select first series search result
    'select_first': False,

    # Always rename files
    'always_rename': False,

    # Batch (same as select_first and always_rename)
    'batch': False,

    # Fail if error finding show data (thetvdb.com is down etc)
    # Only functions when always_rename is True
    'skip_file_on_error': True,

    # Verbose mode (debugging info)
    'verbose': False,

    # Recurse more than one level into folders. When False, only
    # desends one level.
    'recursive': False,

    # When non-empty, only look for files with this extension.
    # No leading dot, for example: ['avi', 'mkv', 'mp4']
    'valid_extensions': [],

    # Force Windows safe filenames (always True on Windows)
    'windows_safe_filenames': False,

    # Replace accented unicode characters with ASCII equivalents,
    # removing characters than can't be translated.
    'normalize_unicode_filenames': False,

    # Replacement characters for invalid filename characters
    'replace_invalid_characters_with': '_',

    # Replacements performed on input file before parsing.
    'input_filename_replacements': [
    ],

    # Replacements performed on files after the new name is generated.
    'output_filename_replacements': [
    ],

    # Language to (try) and retrieve episode data in
    'language': 'en',

    # Search in all possible languages
    'search_all_languages': True,

    # Move renamed files to directory?
    'move_files_enable': False,

    # Destination to move files to. Realtive or absolute paths.
    # Trailing slash is not necessary. Use forward slashes, even on Windows.
    # A value of None or '.' will effectivly disable this.
    #
    # Use Python's string formatting to add dynamic paths. Available variables:
    # - %(seriesname)s
    # - %(seasonnumber)d
    # - %(episodenumber)d
    'move_files_destination': '.',

    # Patterns to parse input filenames with
    'filename_patterns': [
        # [group] Show - 01-02 [Etc]
        '''^\[.+?\][ ]? # group name
        (?P<seriesname>.*?)[ ]?[-_][ ]?          # show name, padding, spaces?
        (?P<episodenumberstart>\d+)              # first episode number
        ([-_]\d+)*                               # optional repeating episodes
        [-_](?P<episodenumberend>\d+)            # last episode number
        [^\/]*$''',

        # [group] Show - 01 [Etc]
        '''^\[.+?\][ ]? # group name
        (?P<seriesname>.*) # show name
        [ ]?[-_][ ]?(?P<episodenumber>\d+)
        [^\/]*$''',

        # foo s01e23 s01e24 s01e25 *
        '''
        ^(?P<seriesname>.+?)[ \._\-]             # show name
        [Ss](?P<seasonnumber>[0-9]+)             # s01
        [\.\- ]?                                 # separator
        [Ee](?P<episodenumberstart>[0-9]+)       # first e23
        ([\.\- ]+                                # separator
        [Ss](?P=seasonnumber)                    # s01
        [\.\- ]?                                 # separator
        [Ee][0-9]+)*                             # e24 etc (middle groups)
        ([\.\- ]+                                # separator
        [Ss](?P=seasonnumber)                    # last s01
        [\.\- ]?                                 # separator
        [Ee](?P<episodenumberend>[0-9]+))        # final episode number
        [^\/]*$''',

        # foo.s01e23e24*
        '''
        ^(?P<seriesname>.+?)[ \._\-]             # show name
        [Ss](?P<seasonnumber>[0-9]+)             # s01
        [\.\- ]?                                 # separator
        [Ee](?P<episodenumberstart>[0-9]+)       # first e23
        ([\.\- ]?                                # separator
        [Ee][0-9]+)*                             # e24e25 etc
        [\.\- ]?[Ee](?P<episodenumberend>[0-9]+) # final episode num
        [^\/]*$''',

        # foo.1x23x24*
        '''
        ^(?P<seriesname>.+?)[ \._\-]             # show name
        (?P<seasonnumber>[0-9]+)                 # 1
        [xX](?P<episodenumberstart>[0-9]+)       # first x23
        ([xX][0-9]+)*                            # x24x25 etc
        [xX](?P<episodenumberend>[0-9]+)         # final episode num
        [^\/]*$''',

        # foo.s01e23-24*
        '''
        ^(?P<seriesname>.+?)[ \._\-]             # show name
        [Ss](?P<seasonnumber>[0-9]+)             # s01
        [\.\- ]?                                 # separator
        [Ee](?P<episodenumberstart>[0-9]+)       # first e23
        (                                        # -24 etc
             [\-]
             [Ee]?[0-9]+
        )*
             [\-]                                # separator
             (?P<episodenumberend>[0-9]+)        # final episode num
        [^\/]*$''',

        # foo.1x23-24*
        '''
        ^(?P<seriesname>.+?)[ \._\-]             # show name
        (?P<seasonnumber>[0-9]+)                 # 1
        [xX](?P<episodenumberstart>[0-9]+)       # first x23
        (                                        # -24 etc
             [\-][0-9]+
        )*
             [\-]                                # separator
             (?P<episodenumberend>[0-9]+)        # final episode num
        [^\/]*$''',

        # foo.[1x09-11]*
        '''^(?P<seriesname>.+?)[ \._\-]          # show name and padding
        \[                                       # [
            ?(?P<seasonnumber>[0-9]+)            # season
        [xX]                                     # x
            (?P<episodenumberstart>[0-9]+)       # episode
            (- [0-9]+)*
        -                                        # -
            (?P<episodenumberend>[0-9]+)         # episode
        \]                                       # \]
        [^\\/]*$''',

        # foo.s0101, foo.0201
        '''^(?P<seriesname>.+?)[ \._\-]
        [Ss](?P<seasonnumber>[0-9]{2})
        [\.\- ]?
        (?P<episodenumber>[0-9]{2})
        [^\\/]*$''',

        # foo.1x09*
        '''^(?P<seriesname>.+?)[ \._\-]          # show name and padding
        \[?                                      # [ optional
        (?P<seasonnumber>[0-9]+)                 # season
        [xX]                                     # x
        (?P<episodenumber>[0-9]+)                # episode
        \]?                                      # ] optional
        [^\\/]*$''',

        # foo.s01.e01, foo.s01_e01
        '''^(?P<seriesname>.+?)[ \._\-]
        [Ss](?P<seasonnumber>[0-9]+)[\.\- ]?
        [Ee]?(?P<episodenumber>[0-9]+)
        [^\\/]*$''',

        # Foo - S2 E 02 - etc
        '''^(?P<seriesname>.+?)[ ]?[ \._\-][ ]?
        [Ss](?P<seasonnumber>[0-9]+)[\.\- ]?
        [Ee]?[ ]?(?P<episodenumber>[0-9]+)
        [^\\/]*$''',

        # Show - Episode 9999 [S 12 - Ep 131] - etc
        '''
        (?P<seriesname>.+)                       # Showname
        [ ]-[ ]                                  # -
        [Ee]pisode[ ]\d+                         # Episode 1234 (ignored)
        [ ]
        \[                                       # [
        [sS][ ]?(?P<seasonnumber>\d+)            # s 12
        ([ ]|[ ]-[ ]|-)                          # space, or -
        ([eE]|[eE]p)[ ]?(?P<episodenumber>\d+)   # e or ep 12
        \]                                       # ]
        .*$                                      # rest of file
        ''',

        # foo.103*
        '''^(?P<seriesname>.+)[ \._\-]
        (?P<seasonnumber>[0-9]{1})
        (?P<episodenumber>[0-9]{2})
        [\._ -][^\\/]*$''',

        # foo.0103*
        '''^(?P<seriesname>.+)[ \._\-]
        (?P<seasonnumber>[0-9]{2})
        (?P<episodenumber>[0-9]{2,3})
        [\._ -][^\\/]*$''',

        # show.name.e123.abc
        '''^(?P<seriesname>.+?)                  # Show name
        [ \._\-]                                 # Padding
        [Ee](?P<episodenumber>[0-9]+)            # E123
        [\._ -][^\\/]*$                          # More padding, then anything
        '''
    ],

    # Formats for renamed files. Variations for with/without episode,
    # and with/without season number.
    'filename_with_episode':
     '%(seriesname)s - [%(seasonno)02dx%(episode)s] - %(episodename)s%(ext)s',
    'filename_without_episode':
     '%(seriesname)s - [%(seasonno)02dx%(episode)s]%(ext)s',
     'filename_with_episode_no_season':
      '%(seriesname)s - [%(episode)s] - %(episodename)s%(ext)s',
     'filename_without_episode_no_season':
      '%(seriesname)s - [%(episode)s]%(ext)s',

    # Used to join multiple episode names together
    'multiep_join_name_with': ', ',

    # Format for numbers (python string format), %02d does 2-digit
    # padding, %d will cause no padding
    'episode_single': '%02d',

    # String to join multiple number
    'episode_separator': '-',
}
