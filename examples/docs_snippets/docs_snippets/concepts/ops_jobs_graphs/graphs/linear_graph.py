# start_marker
from dagster import graph, op, OpExecutionContext


@op
def return_one(context) -> int:
    return 1


@op
def add_one(context: OpExecutionContext, number: int) -> int:
    return number + 1


@graph
def linear():
    add_one(add_one(add_one(return_one())))


# end_marker
