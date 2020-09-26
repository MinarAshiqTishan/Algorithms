# circular queue or ring buffer

"""
 methods:
  * is_full() : check if the queue is full
  * is_empty() : check if the queue is empty
  * enqueue() : add a new item to the back of the queue
  * dequeue() : remove the front value from the queue
  * clearq() : empty the queue

 rules:
  * queue is full if head_index == (tail_index % MAXSIZE) + 1
  * queue is empty if tail_index == head_index
  * adding to queue :
        * check if queue is full.
        * if not, increase tail index by 1 :  tail_index = (tail_index + 1) % MAXSIZE
        * then, add a value to the tail index
  * deleting from queue:
        * check if queue is empty.
        * if not, delete the value at head_index
        * increase head_index : head_index = (head_index + 1) % MAXSIZE
  * clearing the queue : set tail_index = head_index

  Application :
   * scheduler
   * static memory queue
"""



