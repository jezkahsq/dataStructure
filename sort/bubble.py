import random

# 时间复杂度 O(n方)
def bubble_sort(li):
    for i in range(0, len(li)-1):
        # 冒泡排序的每一趟会有一个最大的数去到最后一个
        # 一趟排序完成后，无序区减少一个数，有序区增加一个数
        # 第i趟时，无序区范围是0到len(li)-i- 1
        for j in range(0, len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
        #print(li) # 打印每一趟排完后
    return li


li = [random.randint(0,10) for i in range(10)]
print(li)
print(bubble_sort(li))
