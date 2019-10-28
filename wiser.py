import argparse
from modules import DocumentManager

def main():
    args = parse_args()
    compress_method = args.compress_method
    wikipedia_dump_file = args.wikipedia_dump_xml
    search_query = args.search_query
    max_index_count = args.max_index_count
    ii_buffer_update_threshold = args.ii_buffer_update_threshold
    enable_phrase_search = args.s
    db_path = args.enable_phrase_search

    # TODO: implements インデックス作成モードのときのDB周りのエラー処理

    manager = DocumentManager(db_path,
                              ii_buffer_update_threshold,
                              enable_phrase_search)

    # TODO: implements print_time_diff
    manager.load_wikipedia_dump(wikipedia_dump_file, max_index_count)

def parse_args():
    parser = argparse.ArgumentParser(description='TODO: あとで書く') 
    parser.add_argument('db_path', )
    parser.add_argument('-c', '--compress_method', default=None, help='compress method for postings list')
    parser.add_argument('-x', '--wikipedia_dump_xml', help='wikipedia dump xml path for indexing')
    parser.add_argument('-q', '--search_query', help='query for search')
    parser.add_argument('-m', '--max_index_count', type=int, default=-1, help='max count for indexing document')
    parser.add_argument('-t', '--ii_buffer_update_threshold', type=int, default=DEFAULT_II_BUFFER_UPDATE_THRESHOLD, help='inverted index buffer merge threshold')
    parser.add_argument('-s', 'enable_phrase_search', help="don't use tokens positions for search", action='store_true')
    return parser.parse_args()
