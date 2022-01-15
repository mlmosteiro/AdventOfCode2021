"""
+---+---------------+-----------------------------------------------------------+
|   | A B C D E F G |     len     order         explanation                     |
+---+---------------+-----------------------------------------------------------+
| 1 | A B - - - - - |       2         1         only 2 segments                 |
| 7 | A B - D - - - |       3         2         only 3 segments                 |
| 4 | A B - - E F - |       4         3         only 4 segments                 |
| 2 | A - C D - F G |       5        10         last one with 5 segments        |
| 3 | A B C D - F - |       5         5         5 segments and both from 1      |
| 5 | - B C D E F - |       5         9         5 segments and 6/9 contains all |
| 0 | A B C D E - G |       6         8         last one with 6 segments        |
| 6 | - B C D E F G |       6         6         6 segments and only one from 1  |
| 9 | A B C D E F - |       6         7         6 segments and all from 3       |
| 8 | A B C D E F G |       7         4         only 7 segments                 |
+---+---------------+-----------------------------------------------------------+
"""