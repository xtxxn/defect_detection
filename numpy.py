st_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])#（M行，N列）*（N行，Z列）=（M行，Z列）平时成绩占40% 期末成绩占60%, 计算结果
 q = np.array([[0.4], [0.6]])
 result = np.dot(st_score, q)
print(result)
OriginalY = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print(np.insert(OriginalY, 1, [11, 12, 10]))
print(np.insert(OriginalY, 1, [[11, 12, 10]], axis=0))
# 在列索引1的位置插入（注意元素格式，跟添加格式不同）
 print(np.insert(OriginalY, 1, [[11, 12, 10]], axis=1))



