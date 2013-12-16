# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.

"""
@brief C language specific LOXI generating configuration

This language specific file defines a dictionary 'targets' that
defines the generated files and the functions used to generate them.
"""

import os
import c_gen.of_g_legacy as of_g
import c_gen.build_of_g as build_of_g
import c_gen.c_code_gen as c_code_gen
import c_gen.c_test_gen as c_test_gen
import c_gen.c_dump_gen as c_dump_gen
import c_gen.c_show_gen as c_show_gen
import c_gen.c_validator_gen as c_validator_gen
import c_gen.util
import c_gen.codegen
import loxi_utils.loxi_utils as loxi_utils
import template_utils

def static(out, name):
    c_gen.util.render_template(out, os.path.basename(name))

targets = {
    # LOCI headers
    'loci/inc/loci/loci.h': c_code_gen.top_h_gen,
    'loci/inc/loci/loci_idents.h': c_code_gen.identifiers_gen,
    'loci/inc/loci/loci_base.h': c_code_gen.base_h_gen,
    'loci/inc/loci/of_match.h': c_code_gen.match_h_gen,
    'loci/inc/loci/loci_doc.h': c_code_gen.gen_accessor_doc,
    'loci/inc/loci/loci_obj_dump.h': c_dump_gen.gen_obj_dump_h,
    'loci/inc/loci/loci_obj_show.h': c_show_gen.gen_obj_show_h,
    'loci/inc/loci/loci_validator.h': c_validator_gen.gen_h,

    # Static LOCI headers
    'loci/inc/loci/bsn_ext.h': static,
    'loci/inc/loci/loci_dox.h': static,
    'loci/inc/loci/loci_dump.h': static,
    'loci/inc/loci/loci_show.h': static,
    'loci/inc/loci/of_buffer.h': static,
    'loci/inc/loci/of_doc.h': static,
    'loci/inc/loci/of_message.h': static,
    'loci/inc/loci/of_object.h': static,
    'loci/inc/loci/of_utils.h': static,
    'loci/inc/loci/of_wire_buf.h': static,

    # LOCI code
    'loci/src/of_type_data.c': c_code_gen.type_data_c_gen,
    'loci/src/of_match.c': c_code_gen.match_c_gen,
    'loci/src/loci_obj_dump.c': c_dump_gen.gen_obj_dump_c,
    'loci/src/loci_obj_show.c': c_show_gen.gen_obj_show_c,
    'loci/src/loci_validator.c': c_validator_gen.gen_c,

    # Static LOCI code
    'loci/src/loci_int.h': static,
    'loci/src/loci_log.c': static,
    'loci/src/loci_log.h': static,
    'loci/src/of_object.c': static,
    'loci/src/of_type_maps.c': static,
    'loci/src/of_utils.c': static,
    'loci/src/of_wire_buf.c': static,
    'loci/src/loci_setup_from_add_fns.c': static,

    # Static LOCI documentation
    'loci/README': static,
    'loci/Doxyfile': static,

    # locitest code
    'locitest/inc/locitest/of_dup.h': c_test_gen.dup_h_gen,
    'locitest/inc/locitest/test_common.h': c_test_gen.gen_common_test_header,
    'locitest/src/of_dup.c': c_test_gen.dup_c_gen,
    'locitest/src/test_common.c': c_test_gen.gen_common_test,
    'locitest/src/test_list.c': c_test_gen.gen_list_test,
    'locitest/src/test_match.c': c_test_gen.gen_match_test,
    'locitest/src/test_msg.c': c_test_gen.gen_msg_test,
    'locitest/src/test_scalar_acc.c': c_test_gen.gen_message_scalar_test,
    'locitest/src/test_uni_acc.c': c_test_gen.gen_unified_accessor_tests,
    'locitest/src/test_data.c': c_test_gen.gen_datafiles_tests,

    # Static locitest code
    'locitest/inc/locitest/unittest.h': static,
    'locitest/src/test_ext.c': static,
    'locitest/src/test_list_limits.c': static,
    'locitest/src/test_match_utils.c': static,
    'locitest/src/test_setup_from_add.c': static,
    'locitest/src/test_utils.c': static,
    'locitest/src/test_validator.c': static,
    'locitest/src/main.c': static,
    'locitest/Makefile': static,
}

def generate(install_dir):
    build_of_g.initialize_versions()
    build_of_g.build_ordered_classes()
    build_of_g.populate_type_maps()
    build_of_g.analyze_input()
    build_of_g.unify_input()
    build_of_g.order_and_assign_object_ids()
    for (name, fn) in targets.items():
        with template_utils.open_output(install_dir, name) as outfile:
            fn(outfile, os.path.basename(name))
    c_gen.codegen.generate_classes(install_dir)
    c_gen.codegen.generate_header_classes(install_dir)
    c_gen.codegen.generate_classes_header(install_dir)
    c_gen.codegen.generate_lists(install_dir)
    c_gen.codegen.generate_strings(install_dir)
    c_gen.codegen.generate_init_map(install_dir)
