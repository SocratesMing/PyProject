# 二分查找，一般看到时间复杂度为nlogn的要求就考虑二分法

# 1. 循环退出条件，注意是low <= high，⽽不是low < high。
# 2. mid 的取值，mid := low + ((high-low)>>1)
# 3. low 和high 的更新。low = mid + 1，high = mid - 1。

# 注意python中的>>优先级比较低，因此要注意＋括号  mid := low + ((high-low)>>1)