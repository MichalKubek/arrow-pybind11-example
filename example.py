import pyarrow as pa
import MyModule

arr = pa.array([1, 2, 3])
print(MyModule.run_udf(arr))
print(pa.Table.from_batches([MyModule.batch(5)]))
