# IMPORTS
from file_ops import *
from web_ops import *
from g_drive_ops import *

link_source_file = 'rudolf steiner links.txt'
base_url = 'https://steinerlibrary.org/'
data_file = 'RudolfSteinerData.json'
download_loc = os.path.join(os.getcwd(), 'downloads')
# upload_folder = os.path.join(os.getcwd(), 'upload_sandbox')
upload_files = sort_files_n_dirs(download_loc)['files']

def main():
# file operations ************************************************************

    data = filter_(read_file(link_source_file))
    dict_ = convertAllToDict(data)    
    bulk_dict = convert_to_dict('bulk_data', data)
    dict_.update(bulk_dict)

    if openJsonFile(data_file) == dict_:
        print(f"{data_file} up to date...")
    else:
        write_to_json_file(convert_to_json(dict_),'RudolfSteinerData')

# Web operations ************************************************************
    driver = set_up_driver()

    for i, key in enumerate(dict_['PdfLinks'].keys()):
        file_path = os.path.join(download_loc, dict_['Pdf_Filenames'][i])

        if not os.path.exists(file_path):
            download_file(driver, key, dict_['PdfLinks'][key])
            check_file(file_path)
        else:
            print(f"{key} already exists...")
            
    close_driver(driver)

    print("file(s) downloaded successfully")

    os.system('cls')

# Google drive operations ************************************************************
    get_metadata()
    
    file2 = search_item('IMG_20190809_153812')['files'].pop()
    path = os.path.join(os.getcwd(), file2['name'])

    # print(file, file2)
    read_item(file2, path)

if __name__ == '__main__':
    main() 