import sys
import win32com.client

iTunes = win32com.client.Dispatch("iTunes.Application")
library = iTunes.LibraryPlaylist

library.AddFile(sys.argv[1])