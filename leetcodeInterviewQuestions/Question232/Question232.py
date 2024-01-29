class MyQueue:
      
          def __init__(self):
         """
         Initialize your data structure here.
         """
         self.stack1 = []  # 用于存储数据
         self.stack2 = []  # 用于存储数据
      
          def push(self, x: int) -> None:
         """
         Push element x to the back of queue.
         """
         self.stack1.append(x)  # 将数据压入stack1中
      
          def pop(self) -> int:
         """
         Removes the element from in front of queue and returns that element.
         """
         if not self.stack2:  # 如果stack2为空
              while self.stack1:  # 将stack1中的数据全部压入stack2中
                   self.stack2.append(self.stack1.pop())
         return self.stack2.pop()  # 弹出stack2中的数据
      
          def peek(self) -> int:
         """
         Get the front element.
         """
         if not self.stack2:  # 如果stack2为空
              while self.stack1:  # 将stack1中的数据全部压入stack2中
                   self.stack2.append(self.stack1.pop())
         return self.stack2[-1]  # 返回stack2的栈顶元素
      
          def empty(self) -> bool:
         """
         Returns whether the queue is empty.
         """
         return not self.stack1 and not self.stack2  # 如果stack1和stack2都为空，则返回True