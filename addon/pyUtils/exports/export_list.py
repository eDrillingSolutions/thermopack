"""Module for defining files defining symbols to export from thermopack"""
from datetime import datetime


def get_export_statement(compiler, export_info):
    """
    """
    export_statement = ""
    if export_info["module"] is None:
        if export_info["isBindC"]:
            export_statement = export_info["method"]
        else:
            export_statement = export_info["method"] + "_"
    else:
        if compiler == GNU:
            export_statement = "__" + export_info["module"] \
                + "_MOD_" + export_info["method"]
        elif compiler == IFORT:
            export_statement = export_info["module"] + "_mp_" \
                + export_info["method"] + "_"
        elif compiler == PGF90:
            export_statement = export_info["module"] + "_" \
                + export_info["method"] + "_"
        elif compiler == GENERIC:
            export_statement = "*" + export_info["method"] + "*"

    return export_statement


def get_export_header(linker):
    """
    """
    header = "# File generated by thermopack/addon/pyUtils/exports/export_list.py"
    now = datetime.today().isoformat()
    header += "\n# Time stamp: " + now
    if linker == LD_GCC:
        header += "\nlibthermopack {\n# Explicit list of symbols to be exported\n  global:"
    elif linker == LD_CLANG:
        header += "\n# Explicit list of symbols to be exported"
    elif linker == LD_MSVC:
        header += "\n; @NAME@.def : Declares the module parameters.\n\nLIBRARY\n\nEXPORTS"
    return header


def get_export_footer(linker):
    """
    """
    footer = None
    if linker == LD_GCC:
        footer = "\n  local: *;      # hide everything else\n};"
    return footer


def write_def_file(compiler, linker, filename):
    """
    """
    lines = []
    header = get_export_header(linker)
    lines.append(header)
    for i in range(len(exports)):
        export_statement = get_export_statement(compiler, exports[i])
        if linker == LD_GCC:
            lines.append("\t" + export_statement + ";")
        elif linker == LD_CLANG or linker == LD_MSVC:
            lines.append("\t" + export_statement)
    footer = get_export_footer(linker)
    if footer is not None:
        lines.append(footer)

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            f.write("\n")


def append_export(method, module=None, isBindC=False):
    """ Append export symbol
    """
    exports.append({'method': method, 'module': module, 'isBindC': isBindC})


exports = []

append_export("thermopack_init_c", isBindC=True)
append_export("thermopack_init_c", isBindC=True)
append_export("thermopack_pressure_c", isBindC=True)
append_export("thermopack_specific_volume_c", isBindC=True)
append_export("thermopack_tpflash_c", isBindC=True)
append_export("thermopack_uvflash_c", isBindC=True)
append_export("thermopack_hpflash_c", isBindC=True)
append_export("thermopack_spflash_c", isBindC=True)
append_export("thermopack_bubt_c", isBindC=True)
append_export("thermopack_bubp_c", isBindC=True)
append_export("thermopack_dewt_c", isBindC=True)
append_export("thermopack_dewp_c", isBindC=True)
append_export("thermopack_zfac_c", isBindC=True)
append_export("thermopack_enthalpy_c", isBindC=True)
append_export("thermopack_entropy_c", isBindC=True)
append_export("thermopack_wilsonk_c", isBindC=True)
append_export("thermopack_wilsonki_c", isBindC=True)
append_export("thermopack_getcriticalparam_c", isBindC=True)
append_export("thermopack_moleweight_c", isBindC=True)
append_export("thermopack_compmoleweight_c", isBindC=True)
append_export("thermopack_puresat_t_c", isBindC=True)
append_export("thermopack_entropy_tv_c", isBindC=True)
append_export("thermopack_twophase_dhdt_c", isBindC=True)
append_export("thermopack_guess_phase_c", isBindC=True)
append_export("thermopack_thermo_c", isBindC=True)
append_export("get_phase_flags_c", isBindC=True)

append_export("thermopack_getkij")
append_export("thermopack_setkijandji")
append_export("thermopack_gethvparam")
append_export("thermopack_sethvparam")
append_export("thermopack_get_volume_shift_parameters")
append_export("thermopack_set_volume_shift_parameters")

append_export("get_bp_term", "binaryplot")
append_export("vllebinaryxy", "binaryplot")
append_export("global_binary_plot", "binaryplot")

append_export("comp_index_active", "compdata")
append_export("comp_name_active", "compdata")

append_export("calccriticaltv", "critical")

append_export("specificvolume", "eos")
append_export("zfac", "eos")
append_export("thermo", "eos")
append_export("entropy", "eos")
append_export("enthalpy", "eos")
append_export("compmoleweight", "eos")
append_export("idealenthalpysingle", "eos")

append_export("init_thermo", "eoslibinit")
append_export("init_cubic", "eoslibinit")
append_export("init_cpa", "eoslibinit")
append_export("init_pcsaft", "eoslibinit")
append_export("init_saftvrmie", "eoslibinit")
append_export("init_quantum_cubic", "eoslibinit")
append_export("init_tcpr", "eoslibinit")
append_export("init_quantum_saftvrmie", "eoslibinit")
append_export("init_extcsp", "eoslibinit")
append_export("init_lee_kesler", "eoslibinit")
append_export("init_multiparameter", "eoslibinit")
append_export("init_pets", "eoslibinit")
append_export("init_volume_translation", "eoslibinit")
append_export("redefine_critical_parameters", "eoslibinit")

append_export("internal_energy", "eostv")
append_export("entropytv", "eostv")
append_export("pressure", "eostv")
append_export("thermotv", "eostv")
append_export("enthalpytv", "eostv")
append_export("free_energy", "eostv")
append_export("chemical_potential", "eostv")
append_export("virial_coefficients", "eostv")
append_export("secondvirialcoeffmatrix", "eostv")
append_export("binarythirdvirialcoeffmatrix", "eostv")

append_export("isobar", "isolines")
append_export("isotherm", "isolines")
append_export("isenthalp", "isolines")
append_export("isentrope", "isolines")

append_export("setphtolerance", "ph_solver")
append_export("twophasephflash", "ph_solver")

append_export("twophasepsflash", "ps_solver")

append_export("get_saftvrmie_eps_kij", "saftvrmie_containers")
append_export("set_saftvrmie_eps_kij", "saftvrmie_containers")
append_export("get_saftvrmie_sigma_lij", "saftvrmie_containers")
append_export("set_saftvrmie_sigma_lij", "saftvrmie_containers")
append_export("get_saftvrmie_lr_gammaij", "saftvrmie_containers")
append_export("set_saftvrmie_lr_gammaij", "saftvrmie_containers")
append_export("get_saftvrmie_pure_fluid_param", "saftvrmie_containers")
append_export("set_saftvrmie_pure_fluid_param", "saftvrmie_containers")

append_export("cpa_get_kij", "saft_interface")
append_export("cpa_set_kij", "saft_interface")
append_export("pc_saft_get_kij", "saft_interface")
append_export("pc_saft_set_kij_asym", "saft_interface")

append_export("enable_hs", "saftvrmie_options")
append_export("enable_a1", "saftvrmie_options")
append_export("enable_a2", "saftvrmie_options")
append_export("enable_a3", "saftvrmie_options")
append_export("enable_chain", "saftvrmie_options")

append_export("safe_bubt", "saturation")
append_export("safe_bubp", "saturation")
append_export("safe_dewt", "saturation")
append_export("safe_dewp", "saturation")

append_export("envelopeplot", "saturation_curve")

append_export("solid_init", "solideos")

append_export("solidenvelopeplot", "solid_saturation")

append_export("sound_velocity_2ph", "speed_of_sound")

append_export("guessphase", "thermo_utils")

append_export("rgas", "thermopack_constants")
append_export("tptmin", "thermopack_constants")
append_export("tppmin", "thermopack_constants")

append_export("add_eos", "thermopack_var")
append_export("delete_eos", "thermopack_var")
append_export("activate_model", "thermopack_var")
append_export("get_eos_identification", "thermopack_var")

append_export("twophasetpflash", "tp_solver")

append_export("twophasesvflash", "sv_solver")

append_export("twophaseuvflash", "uv_solver")

# FORTRAN compilers
GNU = 1
IFORT = 2
PGF90 = 3
GENERIC = 4

# Linkers
LD_GCC = 1
LD_CLANG = 2
LD_MSVC = 3

if __name__ == "__main__":
    # Write export files
    write_def_file(GENERIC, LD_GCC, "libthermopack_export.version")
    write_def_file(GENERIC, LD_CLANG, "libthermopack_export.symbols")
    write_def_file(IFORT, LD_MSVC, "thermopack.def")
