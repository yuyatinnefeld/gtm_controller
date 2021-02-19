from pprint import pprint

class GTMTag():

    def __init__(self, workspaces): 
        
        if workspaces:
            self.tags = workspaces.tags()
        else:
            print("workspaces not exist")

    def _create_html(self, workspace_path, tag_info):

        tag = {
            'name': tag_info['tag_name'],
            'type': tag_info['tag_type'],
            'parameter': [
                {'key': 'html', 'type': 'template', 'value': tag_info['script']}
            ],
        }

        try:
            return self.tags.create(parent=workspace_path, body=tag).execute()
        except:
            print("this tag exists")

    def _create_ga_pageview(self, workspace_path, tag_info):

        tag = {
            'name': tag_info['tag_name'],
            'type': tag_info['tag_type'],
            'parameter': [
                {'key': 'trackingId','type': 'template','value': str(tag_info['ua_id']),}
            ],
        }

        try:
            return self.tags.create(parent=workspace_path, body=tag).execute()
        except:
            print("this tag exists")

    def _create_ga_event(self, workspace_path, tag_info):

        tag = {
            'name': tag_info['tag_name'],
            'type': tag_info['tag_type'],
            'parameter': [
                {'key': 'gaSettings', 'type': 'template','value': tag_info['ga_settings']},
                {'key': 'nonInteraction', 'type': 'boolean', 'value': tag_info['non_interaction']},
                {'key': 'trackType', 'type': 'template', 'value': 'TRACK_EVENT'},
                {'key': 'eventCategory', 'type': 'template', 'value': tag_info['event_category']},
                {'key': 'eventAction', 'type': 'template', 'value': tag_info['event_action']},
                {'key': 'eventLabel', 'type': 'template', 'value': tag_info['event_label']},
            ],
        }

        try:
            return self.tags.create(parent=workspace_path, body=tag).execute()
        except:
            print("this tag exists")

    def _create_gads(self, workspace_path, tag_info):

        tag = {
            'name': tag_info['tag_name'],
            'type': tag_info['tag_type'],
            'parameter': [
                {'key': 'conversionId', 'type': 'template', 'value': tag_info['conv_id']},
                {'key': 'conversionLabel', 'type': 'template', 'value': tag_info['conv_label']}
            ]
        }
        
        try:
            return self.tags.create(parent=workspace_path, body=tag).execute()
        except:
            print("this tag exists")
    
    def _create_flc(self, workspace_path, tag_info):
        
        tag = {
            'name': tag_info['tag_name'],
            'type': tag_info['tag_type'],
            'parameter': [
                {'key': 'advertiserId', 'type': 'template', 'value': tag_info['advertiser_id']},
                {'key': 'groupTag', 'type': 'template', 'value': tag_info['group_tag']},
                {'key': 'activityTag', 'type': 'template', 'value': tag_info['activity_tag']},
                {'key': 'ordinalType', 'type': 'template', 'value': tag_info['count_method']},
            ]
        }

        try:
            return self.tags.create(parent=workspace_path, body=tag).execute()
        except:
            print("this tag exists")

    def _create_fls(self, workspace_path, tag_info):
            
        tag = {
            'name': tag_info['tag_name'],
            'type': tag_info['tag_type'],
            'parameter': [
                {'key': 'advertiserId', 'type': 'template', 'value': tag_info['advertiser_id']},
                {'key': 'groupTag', 'type': 'template', 'value': tag_info['group_tag']},
                {'key': 'activityTag', 'type': 'template', 'value': tag_info['activity_tag']},
                {'key': 'ordinalType', 'type': 'template', 'value': tag_info['count_method']},
                {'key': 'orderId', 'type': 'template', 'value': tag_info['order_id']},
                {'key': 'revenue', 'type': 'template', 'value': tag_info['revenue']},
            ]
        }

        try:
            return self.tags.create(parent=workspace_path, body=tag).execute()
        except:
            print("this tag exists")

    def _get_tag_by_name(self, workspace_path, tag_name):
        tags = self.tags.list(parent=workspace_path).execute()
        result = None
        
        for tag in tags['tag']: 
            if (tag['name'] == tag_name):
                result = tag
            else:
                pass
        return result

    def _connect_with_trigger(self, tag, trigger):
        tag = self.tags.get(path=tag['path']).execute()
        tag['firingTriggerId'] = [trigger['triggerId']]
        response = self.tags.update(path=tag['path'],body=tag).execute()

    def _info(self, tag):
        pprint(tag)