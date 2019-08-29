import decision_tree as dtree

data = [['青年', '否', '否', '一般', '否'],
        ['青年', '否', '否', '好', '否'],
        ['青年', '是', '否', '好', '是'],
        ['青年', '是', '是', '一般', '是'],
        ['青年', '否', '否', '一般', '否'],
        ['中年', '否', '否', '一般', '否'],
        ['中年', '否', '否', '好', '否'],
        ['中年', '是', '是', '好', '是'],
        ['中年', '否', '是', '非常好', '是'],
        ['中年', '否', '是', '非常好', '是'],
        ['老年', '否', '是', '非常好', '是'],
        ['老年', '否', '是', '好', '是'],
        ['老年', '是', '否', '好', '是'],
        ['老年', '是', '否', '非常好', '是'],
        ['老年', '否', '否', '一般', '否'],]
labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
mytree = dtree.create_tree(data, labels)
print(mytree)

testdata = ['青年', '否', '否', '非常好']
testlabel = ['年龄', '有工作', '有自己的房子', '信贷情况']
# 由于在生成决策树模型的时候labels有所改动，所以分类预测时不能直接调用labels
result = dtree.classify(mytree, testlabel, testdata)
print(result)


