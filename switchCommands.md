| **These all appear to be action codes, not getting data codes** |
| --------------------------------------------------------------- |
|                                                                 |  |  |
|                                                                 |  |  |
|                                                                 |  |  |
| **Command**                                                     |  |  |
| **102**                                                         | (update firmware) |  |
| **103**                                                         | (reload ports) | //Single Choice |
|                                                                 |  | code = 1 << 0x9 \| portIndex[port] << 0x4 \| 3; |
| **104**                                                         | (reboot switch) |  |
| **105**                                                         | (reset to factory defaults) |
| **120**                                                         | (Reset password) | Original_Key |
|                                                                 |  | New_key |
| **123**                                                         | (login function) |  |
| **127**                                                         | (enable lldp) | This is the adaptive power supply feature |
| **201**                                                         | (backup switch configuration) |
