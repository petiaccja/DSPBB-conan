from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
import os

class DSPBBConan(ConanFile):
    name = "dspbb"
    license = "MIT"
    homepage = "https://github.com/petiaccja/DSPBB"
    url = "https://github.com/conan-io/conan-center-index/"
    description = "Modern library for digital signal processing."
    topics = ("digital-signal-processing", "iir-filters", "fir-filters", "filter-design", "math", "dsp", "signals", "statistics")
    no_copy_source = True
    settings = "compiler"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _compilers_minimum_version(self):
        return {
            "apple-clang": 10,
            "clang": 6,
            "gcc": 7,
            "Visual Studio": 16,
        }

    def configure(self):
        if self.settings.compiler.cppstd:
            tools.check_min_cppstd(self, "17")

        minimum_version = self._compilers_minimum_version.get(str(self.settings.compiler), False)
        if minimum_version:
            if tools.Version(self.settings.compiler.version) < minimum_version:
                raise ConanInvalidConfiguration("dspbb requires C++17, which your compiler does not support.")
        else:
            self.output.warn("dspbb requires C++17. Your compiler is unknown. Assuming it supports C++17.")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("DSPBB-" + self.version, self._source_subfolder)

    def requirements(self):
        for req in self.conan_data["requirements"][self.version]:
            self.requires(req)
            
    def package(self):
        self.copy("*.hpp", dst=os.path.join("include", "dspbb"), src=os.path.join(self._source_subfolder, "include", "dspbb"))
        self.copy("*.h", dst=os.path.join("include", "dspbb"), src=os.path.join(self._source_subfolder, "include", "dspbb"))
        self.copy("LICENSE.md", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
