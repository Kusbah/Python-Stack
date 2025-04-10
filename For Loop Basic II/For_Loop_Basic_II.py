#Biggie Size
# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#     return list
# print(biggie_size([-1, 3, 5, -5]) )
#Count Positives 
# def count_positives(list):
#     num = 0
#     for i in range(len(list)):
#         if list[i]>0:
#             num +=1
#     list[len(list)-1]=num
#     return list
# print(count_positives([1,6,-4,-2,-7,-2]))
#Sum Total
# def sum_total(list):
#     sum = 0
#     for i in range (len(list)):
#        sum += list[i]
#     return sum
# print(sum_total([6,3,-2]))
#Average
# def average(list):
#     sum = 0
#     for i in range (len(list)):
#        sum += list[i]
#     sum/= len(list)
#     return sum
# print(average([6,3,-2]))
#Length
# def length(list):
#     return len(list)
# print(length([37,2,1,-9]) )
#Minimum
# def minimum(list):
#     if len(list)==0:
#         return False
#     min = list[0]
#     for i in range (len(list)):
#         if list[i] < min:
#             min = list[i]
#     return min
# print(minimum([37,2,1,-9]))
#Maximum 
# def maximum(list):
#     if len(list)==0:
#         return False
#     max = list[0]
#     for i in range (len(list)):
#         if list[i] > max:
#             max = list[i]
#     return max
# print(maximum([37,2,1,-9]))
#Ultimate Analysis
# def ultimate_analysis(list):
#     if len(list) == 0:
#         return False
    
#     total = 0
#     max_val = list[0]
#     min_val = list[0]
    
#     for i in range(len(list)):
#         total += list[i]
#         if list[i] > max_val:
#             max_val = list[i]
#         if list[i] < min_val:
#             min_val = list[i]
#     avg = total / len(list)
#     print(f"sumTotal: {total}, average: {avg}, minimum: {min_val}, maximum: {max_val}, length: {len(list)}")
#     return total,max_val,min_val,avg
# ultimate_analysis([37,2,1,-9])
#Reverse List
# def reverse_list(list):
#     for i in range(len(list) // 2):
#         temp = list[i]
#         list[i] = list[len(list) - 1 - i]
#         list[len(list) - 1 - i] = temp
#     return list

# print(reverse_list([37, 2, 1, -9])) 
