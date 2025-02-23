""" ksconf - Ksconf Splunk CONFig tool


Design goals:

 * Multi-purpose go-to ``.conf`` tool.
 * Dependability
 * Simplicity
 * No eternal dependencies (single source file, if possible; or packable as single file.)
 * Stable CLI
 * Good scripting interface for deployment scripts and/or git hooks

"""

from __future__ import absolute_import, unicode_literals

__author__ = "Lowell Alleman <lowell@kintyre.co>"
__copyright__ = "(c) 2019 Kintyre Solutions, Inc"
__license__ = "Apache Public License v2"

# _version.py is autogenerated at build time.  But is missing on first call to setup.py
try:
    from ._version import build as __build__, vcs_info as __vcs_info__, version as __version__
except ImportError:     # pragma: no cover
    __version__ = None
    __build__ = None
    __vcs_info__ = None


class KsconfPluginWarning(Warning):
    pass


# Because how do you pick just just ONE?!!
__ascii_sigs__ = (
    """
                                  #
                                  ##
 ###  ##     #### ###### #######  ###  ##  #######
 ### ##     ###  ###           ## #### ##
 #####      ###  ###      ##   ## #######  #######
 ### ##     ###  ###      ##   ## ### ###  ##
 ###  ## #####    ######   #####  ###  ##  ##
                                        #
""", """
.-..-. .--.                    .--.
: :' ;: .--'                  : .-'
:   ' `. `.  .--.  .--. ,-.,-.: `;
: :.`. _`, :'  ..'' .; :: ,. :: :
:_;:_;`.__.'`.__.'`.__.':_;:_;:_;
""", r"""
 ___  ____           ______                     ___
|_  ||_  _|        .' ___  |                  .' ..]
  | |_/ /    .--. / .'   \_|  .--.   _ .--.  _| |_
  |  __'.   ( (`\]| |       / .'`\ \[ `.-. |'-| |-'
 _| |  \ \_  `'.'.\ `.___.'\| \__. | | | | |  | |
|____||____|[\__) )`.____ .' '.__.' [___||__][___]
""", r"""
 _  __ __   ___ __  __  _ ___
| |/ /' _/ / _//__\|  \| | __|
|   <`._`.| \_| \/ | | ' | _|
|_|\_\___/ \__/\__/|_|\__|_|
""", r"""
 _                         __
| |                       / _|
| | _____  ___ ___  _ __ | |_
| |/ / __|/ __/ _ \| '_ \|  _|
|   <\__ \ (_| (_) | | | | |
|_|\_\___/\___\___/|_| |_|_|
""", r"""
 _                             ___
| |                           / __)
| |  _  ___  ____ ___  ____ _| |__
| |_/ )/___)/ ___) _ \|  _ (_   __)
|  _ (|___ ( (__| |_| | | | || |
|_| \_|___/ \____)___/|_| |_||_|
""", """
 _                   ___
| |_ ___ ___ ___ ___|  _|
| '_|_ -|  _| . |   |  _|
|_,_|___|___|___|_|_|_|
""", """
kkkkkkkk                                                                                    ffffffffffffffff
k::::::k                                                                                   f::::::::::::::::f
k::::::k                                                                                  f::::::::::::::::::f
k::::::k                                                                                  f::::::fffffff:::::f
 k:::::k    kkkkkkk  ssssssssss       cccccccccccccccc   ooooooooooo   nnnn  nnnnnnnn     f:::::f       ffffff
 k:::::k   k:::::k ss::::::::::s    cc:::::::::::::::c oo:::::::::::oo n:::nn::::::::nn   f:::::f
 k:::::k  k:::::kss:::::::::::::s  c:::::::::::::::::co:::::::::::::::on::::::::::::::nn f:::::::ffffff
 k:::::k k:::::k s::::::ssss:::::sc:::::::cccccc:::::co:::::ooooo:::::onn:::::::::::::::nf::::::::::::f
 k::::::k:::::k   s:::::s  ssssss c::::::c     ccccccco::::o     o::::o  n:::::nnnn:::::nf::::::::::::f
 k:::::::::::k      s::::::s      c:::::c             o::::o     o::::o  n::::n    n::::nf:::::::ffffff
 k:::::::::::k         s::::::s   c:::::c             o::::o     o::::o  n::::n    n::::n f:::::f
 k::::::k:::::k  ssssss   s:::::s c::::::c     ccccccco::::o     o::::o  n::::n    n::::n f:::::f
k::::::k k:::::k s:::::ssss::::::sc:::::::cccccc:::::co:::::ooooo:::::o  n::::n    n::::nf:::::::f
k::::::k  k:::::ks::::::::::::::s  c:::::::::::::::::co:::::::::::::::o  n::::n    n::::nf:::::::f
k::::::k   k:::::ks:::::::::::ss    cc:::::::::::::::c oo:::::::::::oo   n::::n    n::::nf:::::::f
kkkkkkkk    kkkkkkksssssssssss        cccccccccccccccc   ooooooooooo     nnnnnn    nnnnnnfffffffff
""", r"""
 _                         __
| | _____  ___ ___  _ __  / _|
| |/ / __|/ __/ _ \| '_ \| |_
|   <\__ \ (_| (_) | | | |  _|
|_|\_\___/\___\___/|_| |_|_|
""", r"""
 _                         __
| | _____  ___ ___  _ __  / _|
| |/ / __|/ __/ _ \| '_ \| |_
|   <\__ \ (_| (_) | | | |  _|
|_|\_\___/\___\___/|_| |_|_|
""")
