# wireshark-http-gunzip
Decode gzip in Wireshark "Follow SSL Stream" raw files

Unfortunately Wireshark can decode gzip OR decode SSL.
If you have both, you need to do a little work.  This
script runs on saved Raw format files from "Follow SSL Stream"
and shows the unzipped data.
