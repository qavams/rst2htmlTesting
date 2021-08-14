import docutils.core
  
docutils.core.publish_file(
    source_path='pos.rst',
    destination_path='pos.html',
    writer_name ="html",
    settings_overrides={'input_encoding': 'UTF-8', 'output_encoding': 'UTF-8'}
    )
