                                                                                                                                                                                         
#!/usr/bin/env python3

from google.cloud import storage

f = open("myText.txt", "w")
f.write("Yo\n")
f.write("awe")
f.close()

def upload_blob(bucket_name, source_file_name, destination_blob_name):
  """Uploads a file to the bucket."""


  storage_client = storage.Client()

  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  blob.upload_from_filename(source_file_name)


  print('File {} uploaded to {}.'.format(
      source_file_name,
      destination_blob_name))


upload_blob('test_buk123', 'myText.txt', "myTextOnline.txt")
