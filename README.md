#pharmacy_counting

For this problem, I first read the data into a dictionary with key is the drug name and value is a list consisting of [total_cost, names of individuals prescribed the medication]. Dictionary is the optimal choice of data structure for this task since the dictionary uses hash-table so accessing to a dictionary item is fast and scalable, at order of O(1).

Next for each drug, I need to count number of unique individuals who prescribed the medication. To to so, I convert a list to a set to remove the duplications. Then size of the set is the number of unique individuals who prescribed the medication.

Last, I use the python standard library function sorted() to sort the drug list by total cost then drug name in descending order.

For reading and writing data, I use Python csv standard library.

# Note to Insight Data Engineering
In order to pass the test_1 case, the data for medicine cost should be store in integer but not float. However, this is not correct as we can see in the large data sample, 24 million records, cost of medicine is not always integer, especially some medicines has total cost is just fraction of 1 dollar.
