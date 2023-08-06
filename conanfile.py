from conan import ConanFile
from conan import tools

import os

class DSPBBConan(ConanFile):
    name = "dspbb"

    # Metadata
    license = "MIT"
    homepage = "https://github.com/petiaccja/DSPBB"
    url = "https://github.com/conan-io/conan-center-index/"
    description = "Modern library for digital signal processing."
    topics = ("digital-signal-processing", "iir-filters", "fir-filters", "filter-design", "math", "dsp", "signals", "statistics")

    # Configuration
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return os.path.join(self.source_folder, "source_subfolder")
    
    def source(self):
        tools.files.get(
            self,
            **self.conan_data["sources"][self.version],
            destination=self._source_subfolder,
            strip_root=True
        )

    def requirements(self):
        for req in self.conan_data["requirements"][self.version]:
            self.requires(req)
            
    def package(self):
        src_folder = os.path.join(self._source_subfolder, "include")
        dst_folder = os.path.join(self.package_folder, "include")
        lic_folder = os.path.join(self.package_folder, "licenses")

        tools.files.copy(self, "*.hpp", dst=dst_folder, src=src_folder)
        tools.files.copy(self, "*.h", dst=dst_folder, src=src_folder)
        tools.files.copy(self, "LICENSE.md", dst=lic_folder, src=self._source_subfolder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []

    def package_id(self):
        self.info.clear()
