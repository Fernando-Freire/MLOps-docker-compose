from feast import FeatureService
from feature_views import sample_products_stats_view, test_products_stats_view

sample_products_stats_fs = FeatureService(
    name="sample_products_activity", features=[sample_products_stats_view]
)

test_products_stats_fs = FeatureService(
    name="test_products_activity", features=[test_products_stats_view]
)
