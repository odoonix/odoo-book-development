.. Odoo book development documentation master file


.. Resources & References:
   The main reference is https://www.cybrosys.com/odoo/odoo-books/odoo-18-development
   We translate from en to fa

   here is list of chapters:

   - introduction
   - about/index
   - setup-development-environment/index
   - creating-odoo-modules/index
   - server-side-development/index
   - data-management/index
   - views/index
   - security/index
   - internationalization/index
   - web-development/index
   - website-development/index
   - odoo-web-library/index
   - test-cases/index
   - odoo-sh/index
   - remote-procedure-calls-rpc/index
   - performance-optimisation/index
   - emails/index
   - pos/index
   - iot-box/index
   - others/index
   - appendex/index

   related to each chapter there is a online document.


   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/about/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/set-up-development-environment/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/creating-odoo-modules/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/server-side-development/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/data-management/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/views/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/security/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/internationalization/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/web-development/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/website-development/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/odoo-web-library/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/test-cases/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/odoo-sh/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/remote-procedure-calls-rpc/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/performance-optimisation/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/emails/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/point-of-sales/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/iot-box/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/others/
   #. https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/conclusion/



   ## Docuemnt Structure

   There are a tree struction. The main file is index.rst that contains the toctree of 
   all chapters. each chapter is linked to a folder by name. for example the following 
   contetn is a chapter:

   .. code-block:: none
      
      https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/creating-odoo-modules/

   so there is a folder named 

   creating-odoo-modules

   There is index.rst file in each folder that contains link to all parts with toctree. the
   file path is

   creating-odoo-modules/index.rst

   for each part there is rst file in the chapter folder.

   for example

   https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/creating-odoo-modules/adding-models


   there is a file

   creating-odoo-modules/adding-models.rst


   and the adding-models is added to the toc tree in index.rst

   .. toctree::
   :maxdepth: 2
   :caption: فهرست مطالب:

   adding-models


کتاب اودوو: توسعه و برنامه نویسی
===========================================


.. toctree::
   :maxdepth: 1
   :caption: فهرست مطالب:

   introduction
   about/index

   setup-development-environment/index

   creating-odoo-modules/index
   server-side-development/index
   data-management/index
   views/index
   security/index
   internationalization/index
   web-development/index
   website-development/index
   odoo-web-library/index
   test-cases/index
   odoo-sh/index
   remote-procedure-calls-rpc/index
   performance-optimisation/index
   emails/index
   point-of-sales/index
   iot-box/index
   others/index

   appendex/index
