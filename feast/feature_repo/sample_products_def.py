# This is an example feature definition file

from datetime import timedelta

from feast import Entity, FeatureService, FeatureView, Field, FileSource
from feast.types import Int64, String, UnixTimestamp, Float64

# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
sample_products_stats = FileSource(
    name="sample products",
    path="/feature_repo/data/sample_products.parquet",
    timestamp_field="creation date",
    created_timestamp_column="creation date",
)

# Define an entity for the driver. You can think of entity as a primary key used to
# fetch features.
sample_products = Entity(name="products", join_keys=["product_id"])

# Our parquet files contain sample data that includes a driver_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.
sample_products_stats_view = FeatureView(
    name="sample_products_stats",
    entities=[sample_products],
    ttl=timedelta(days=0),
    schema=[
        Field(name="product_id", dtype=Int64),
        Field(name="seller_id", dtype=Int64),
        Field(name="query", dtype=String),
        Field(name="search_page", dtype=Int64),
        Field(name="position", dtype=Int64),
        Field(name="title", dtype=String),
        Field(name="concatenated_tags", dtype=String),
        Field(name="creation_date", dtype=UnixTimestamp),
        Field(name="price", dtype=Float64),
        Field(name="weight", dtype=Float64),
        Field(name="express_delivery", dtype=Int64),
        Field(name="minimum_quantity", dtype=Int64),
        Field(name="view_counts", dtype=Int64),
        Field(name="order_counts", dtype=Float64),
        Field(name="category", dtype=String),
    ],
    online=False,
    source=sample_products_stats,
    tags={},
)

# product_id             int64 check
# seller_id              int64 check
# query                 object no check -> string
# search_page            int64 check
# position               int64 check 
# title                 object no check -> string
# concatenated_tags     object no check -> string
# creation_date         object no check -> datetime64[ns]
# price                float64 check
# weight               float64 check
# express_delivery       int64 check
# minimum_quantity       int64 check
# view_counts            int64 check
# order_counts         float64 check
# category              object no check -> string


sample_products_stats_fs = FeatureService(
    name="sample_products_activity", features=[sample_products_stats_view]
)


 