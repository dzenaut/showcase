# get the modules we will use
import package1.module1
import package1.module2
import package2.module1
import package2.module2

# alternative: import individual objects from a module to make them available without qualification
from package1.module1 import test

package1.module1.test()

package1.module2.test()

package2.module1.test()

package2.module2.test()

test()
