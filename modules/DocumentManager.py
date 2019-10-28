import DocumentIndexer, DocumentSearcher, models

class DocumentManager:
    def __init__(self, db_path, ii_buffer_update_threshold, enable_phrase_search):
        self.ii_buffer_update_threshold = ii_buffer_update_threshold
        self.db_session = self._init_database(db_path)
        self.indexer = DocumentIndexer(db_session)
        self.searcher = DocumentSearcher(db_session, enable_phrase_search)

    def load_wikipedia_dump(self, wikipedia_dump_file, max_index_count):
      if not wikipedia_dump_file:
          raise Exception()
      self.indexer.load_wikipedia_dump(wikipedia_dump_file, max_index_count)

    def _init_database(db_path):
        engine = models.create_engine(db_path)
        models.create_tables(engine)
        session = models.create_session(engine)
        return session
