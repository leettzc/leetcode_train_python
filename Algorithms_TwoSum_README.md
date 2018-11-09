# leetcode_train_python
day1:Oct 24,2018 Algorithms_Two_Sum.py
day2:Oct 25,2018 Algorithms_Reverse_Integer.py
day3:Oct 29,2018 Algorithms_Palindrome_Number.py#回文：偶数长度可以只取一般，奇数长度可以去掉中间数
day4:Oct 30,2018 Algorithms_longest_substring_without_repeating_characters.py#若遇到列表中没有i：列表依次存储i;若遇到列表中已有i:保存列表长度，取列表中重复字符后的元素作为新列表，将字符i加入列表。
day5:Oct 31，Algorithms_roman_to_integer.py##从最高单位开始遍历{统计listroman[i]的个数并求和，定位最后一个listroman[i]的位置，将所有listroman[i]替换为‘Q’，遍历最后一个listroman[i]前的字符{遍历listroman[i]后面的单位{统计listroman[i + 1 + n]的个数，减去listroman[i + 1 + n]的值，替换掉listroman[i]前面的j个listroman[i + 1 + n]}}删除listroman[i]及其前面的数}。
day6:Nov 1，2018 Algorithms_integer_to_roman.py 将所有可能出现的13种罗马字符从大到小依次排列，用num依次除以罗马单位取整，并减去取得的单位。
day7:Nov 2，2018 Algorithms_Median_of_Two_Sorted_Arrays.py 将两个list合成一个，分奇数、偶数两种情况讨论中位数。
day8:Nov 5,2018 Algorithms_Zigzag_Conversion.py有待提高效率
day9:Nov 7,2018 Algorithms_longest_palindromic_substring.py 分情况讨论
day10:Nov 8,2018 Algorithms_Container_With_Most_Water.py 从两边往中间走，小的就往中间走一步
