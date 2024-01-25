import forum, comment, person, post, organisation, place, tag, tagclass


def populate_static_vertex_mapping():
    return {
        "organisation": organisation.organisation,
        "place": place.place,
        "tag": tag.tag,
        "tagClass": tagclass.tagClass,
    }


def populate_dynamic_vertex_mapping():
    return {
        "comment": comment.comment,
        "forum": forum.forum,
        "person": person.person,
        "post": post.post,
    }


def populate_static_edge_mapping():
    return {
        "organisation_isLocatedIn_place": organisation.organisation_isLocatedIn_place,
        "place_isPartOf_place": place.place_isPartOf_place,
        "tag_hasType_tagclass": tag.tag_hasType_tagclass,
        "tagClass_isSubclassOf_tagclass": tagclass.tagClass_isSubclassOf_tagclass,
    }


def populate_dynamic_edge_mapping():
    return {
        "comment_hasCreator_person": comment.comment_hasCreator_person,
        "comment_hasTag_tag": comment.comment_hasTag_tag,
        "comment_isLocatedIn_place": comment.comment_isLocatedIn_place,
        "comment_replyOf_comment": comment.comment_replyOf_comment,
        "comment_replyOf_post": comment.comment_replyOf_post,
        "forum_containerOf_post": forum.forum_containerOf_post,
        "forum_hasMember_person": forum.forum_hasMember_person,
        "forum_hasModerator_person": forum.forum_hasModerator_person,
        "forum_hasTag_tag": forum.forum_hasTag_tag,
        "person_email_emailaddress": person.person_email_emailaddress,
        "person_hasInterest_tag": person.person_hasInterest_tag,
        "person_isLocatedIn_place": person.person_isLocatedIn_place,
        "person_knows_person": person.person_knows_person,
        "person_likes_comment": person.person_likes_comment,
        "person_likes_post": person.person_likes_post,
        "person_speaks_language": person.person_speaks_language,
        "person_studyAt_organisation": person.person_studyAt_organisation,
        "person_workAt_organisation": person.person_workAt_organisation,
        "post_hasCreator_person": post.post_hasCreator_person,
        "post_hasTag_tag": post.post_hasTag_tag,
        "post_isLocatedIn_place": post.post_isLocatedIn_place
    }
